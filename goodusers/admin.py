from django.contrib import admin, messages
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext as _  # @UnusedImport

from .models import (
                     GoodUser, GoodUserRaw
                     )
from photos.models import Photo
from friends.models import Friend


from libs.instagram.tools import (
                                  InstagramSession, BestPhotos,
                                  BestFollowers
                                  )

   
class GoodUserAdmin(admin.ModelAdmin):
    '''Definition of Admin interface for GoodUsers model'''                                                          
    
    l_instagram_api_limit = 0
    l_instagram_api_limit_start = 0
    l_instagram_api_limit_end = 0
    
    #l_find_top_n_photos = 10
    l_find_top_n_photos = settings.GOODUSERS_FIND_TOP_N_PHOTOS
    l_search_last_photos = settings.GOODUSERS_SEARCH_N_PHOTOS
                                      
                                      
    def analyze_gooduser_find_friends(self, request, queryset):
        '''Action -> Analyze GoodUsers followers and find potential
           Friends.
        '''
        
        l_analyzed_followers = 0
        l_found_friends = 0
        l_analyzed_goodusers = 0
        
        queryset = queryset.filter(to_be_processed=True)
        
        ig_session = InstagramSession(p_is_admin=True, p_token='')
        ig_session.init_instagram_API()
        
        self.l_instagram_api_limit_start, self.l_instagram_api_limit = \
             ig_session.get_api_limits()
        
        for obj in queryset:
            obj.to_be_processed_for_friends = False
            obj.last_processed_friends_date = timezone.datetime.now()
            obj.times_processed_for_friends = obj.times_processed_for_friends + 1
            '''get Instagram user data'''
            self.l_instagram_api_limit_start, self.l_instagram_api_limit = \
                 ig_session.get_api_limits()
                 
            if (ig_session) and \
               (self.l_instagram_api_limit_start > (settings.FRIENDS_TR_ANALYZE_N_FRIENDS + 50)):
                '''We have Instagram session and enough API call remaining'''
                user_search = ig_session.is_instagram_user_valid(obj.instagram_user_name)
                
                if user_search:
                    instagram_user = ig_session.get_instagram_user(user_search[0].id)
                    
                    if instagram_user:
                        l_instagram_user_id = instagram_user.id  
                        l_number_of_followers = instagram_user.counts[u'followed_by']
                        if l_number_of_followers < settings.FRIENDS_TR_ANALYZE_N_FRIENDS:
                            l_analyze_n_followers = l_number_of_followers
                        else:
                            l_analyze_n_followers = settings.FRIENDS_TR_ANALYZE_N_FRIENDS
                        
                        l_best_instagram_followers = \
                            BestFollowers(l_instagram_user_id, l_analyze_n_followers, ig_session)
                            
                        l_instagram_friends = \
                            l_best_instagram_followers.get_best_instagram_followers()
                        l_analyzed_goodusers += 1
                        
                        if l_instagram_friends:
                            '''Found followers - save them to our database'''
                            for follower in l_instagram_friends:
                                l_analyzed_followers += 1
                                l_exists = Friend.objects.filter(instagram_user_id=follower.id)
                                
                                if l_exists.count() == 0:
                                    '''Friend does not exist - add new'''
                                    l_new_friend = \
                                        Friend(instagram_user_id=follower.id,
                                               instagram_user_name=follower.username, instagram_user_name_valid=True,
                                               gooduser=obj, instagram_user_full_name=follower.full_name,
                                               instagram_profile_picture_URL=follower.profile_picture,
                                               instagram_user_bio=follower.bio,
                                               instagram_user_website_URL=follower.website,
                                               is_user_active=True,
                                               number_of_followers=follower.counts[u'followed_by'],
                                               number_of_followings=follower.counts[u'follows'],
                                               number_of_media=follower.counts[u'media'],
                                               instagram_user_profile_page_URL=self.generate_instagram_profile_page_URL(follower.username),
                                               iconosquare_user_profile_page_URL=self.generate_iconosquare_profile_page_URL(follower.id)
                                               )
                                    l_new_friend.save()
                                    l_found_friends += 1
                                else:
                                    '''Friend exists - add new gooduser'''
                                    l_exists.gooduser.add(obj)
                                    l_exists.save()
                                    pass
            
                obj.save()    
        #FRIENDS_TR_ANALYZE_N_FRIENDS
        
        buf = 'Analyzed %s Goodusers. Analyzed %s folowers. Found %s Friends' \
               % (l_analyzed_goodusers, l_analyzed_followers, l_found_friends)
        self.message_user(request, buf)
    analyze_gooduser_find_friends.short_description = 'Find new friends from GoodUser'         
                                                                                
    def analyze_gooduser(self, request, api, p_gooduser):
        '''Do the processing of Good User with Instagram API
           
           Parameters:
           p_gooduser - one GoodUser we want to process
        '''
        
        if api:
                user_search = api.is_instagram_user_valid(p_gooduser.instagram_user_name)
            
        if user_search:
            instagram_user = api.get_instagram_user(user_search[0].id)
                
            p_gooduser.number_of_followers = instagram_user.counts[u'followed_by']
            p_gooduser.number_of_followings = instagram_user.counts[u'follows']
            p_gooduser.number_of_media = instagram_user.counts[u'media']
            p_gooduser.instagram_user_name = instagram_user.username
            p_gooduser.instagram_user_full_name = instagram_user.full_name
            p_gooduser.instagram_user_id = instagram_user.id
            p_gooduser.instagram_profile_picture_URL = instagram_user.profile_picture
            p_gooduser.instagram_user_bio = instagram_user.bio  
            p_gooduser.instagram_user_website_URL = instagram_user.website
            p_gooduser.instagram_user_name_valid = True
        else:
            p_gooduser.instagram_user_name_valid = False
            buf = "analyze_gooduser: ERR-00008 Could not find user %s on Instagram." % (p_gooduser.instagram_user_name)
            self.message_user(request, buf, level=messages.ERROR)    
               
        return p_gooduser    
    
    
    def process_gooduser(self, request, queryset):
        '''Action -> Do what is needed to process a GoodUser with Instagram API
           Process only users that are marked to be processed -> to_be_processed==True
        '''
        
        queryset = queryset.filter(to_be_processed=True)
        l_counter = 0
        l_counter_pics = 0
        
        ig_session = InstagramSession(p_is_admin=True, p_token='')
        ig_session.init_instagram_API()
        
        self.l_instagram_api_limit_start, self.l_instagram_api_limit = \
             ig_session.get_api_limits()
        
        for obj in queryset:
            obj.to_be_processed = False
            obj.last_processed_date = timezone.datetime.now()
            obj.times_processed = obj.times_processed + 1
            obj.instagram_user_profile_page_URL = self.generate_instagram_profile_page_URL(obj.instagram_user_name)
            obj.iconosquare_user_profile_page_URL = self.generate_iconosquare_profile_page_URL(obj.instagram_user_id)
            '''get Instagram user data'''
            obj = self.analyze_gooduser(request, ig_session, obj)
            
            '''Analyze photos of this user'''
            l_best_photos = BestPhotos(obj.instagram_user_id, self.l_find_top_n_photos, 
                                       self.l_search_last_photos, ig_session
                                       )
            l_best_photos.get_instagram_photos()
            l_top_photos = None
            if l_best_photos.l_user_has_photos:
                l_best_photos.get_top_photos()
                l_top_photos = l_best_photos.top_photos_list
            
            obj.save()
            
            '''Delete old best photos for this user'''
            Photo.objects.filter(good_user_id=obj.pk).delete()
            
            '''Insert new best photos for this user'''
            if l_top_photos:
                for val in l_top_photos:
                    rec = Photo(instagram_photo_id=val[0], photo_rating=val[1], good_user_id=obj)
                    rec.save()
                    l_counter_pics += 1

                                     
            
            l_counter += 1

        self.l_instagram_api_limit_end, self.l_instagram_api_limit = \
             ig_session.get_api_limits()
             

                     
        if l_counter == 1:
            buf = '1 user processed successfully (%s photos). Instagram API (%s - %s/%s / diff: %s)' % \
                    (l_counter_pics, self.l_instagram_api_limit_start, self.l_instagram_api_limit_end, 
                     self.l_instagram_api_limit, (int(self.l_instagram_api_limit_start) - int(self.l_instagram_api_limit_end))
                     )
        else:
            buf = '%s user processed successfully (%s photos).  Instagram API (%s - %s/%s / diff: %s)' % \
                    (l_counter, l_counter_pics, self.l_instagram_api_limit_start, self.l_instagram_api_limit_end, 
                     self.l_instagram_api_limit, (int(self.l_instagram_api_limit_start) - int(self.l_instagram_api_limit_end))
                     )
        
    
        self.message_user(request, buf)
    process_gooduser.short_description = 'Process Good User by Instagram API' 
    
    
    def set_goodusers_process_true(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected GoodUsers to True.
           Process only GoodUsers that have flag to_be_processed set to False.
           to_be_processed==False
        '''
        
        queryset = queryset.filter(to_be_processed=False)
        l_counter = 0
        
        for obj in queryset:
            obj.to_be_processed = True        
            obj.save()
            l_counter += 1
        
        self.message_user(request, '%s user(s) flagged to "To Be Processed" successfully.' % (l_counter))
    set_goodusers_process_true.short_description = 'Set "To Be Processed" to "Yes"' 


    def set_goodusers_process_false(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected GoodUsers to False.
           Process only GoodUsers that have flag to_be_processed set to True.
           to_be_processed==True
        '''
        
        queryset = queryset.filter(to_be_processed=True)
        l_counter = 0
        
        for obj in queryset:
            obj.to_be_processed = False        
            obj.save()
            l_counter += 1
        
        self.message_user(request, '%s user(s) flagged to "Not To Be Processed" successfully.' % (l_counter))
    set_goodusers_process_false.short_description = 'Set "To Be Processed" to "No"'  
    
    def generate_instagram_profile_page_URL(self, p_instagram_user_name):
        '''Generate Instagram.com profile page URL for the user
        
        Parameters:
        p_instagram_user_name: Instagram user name, used to generate URL for profile page
        
        Returns:
        URL of Instagram profile page for this GoodUser
        '''
        
        l_instagram_profile_page_URL = 'http://www.instagram.com/%s' % (p_instagram_user_name)
        return l_instagram_profile_page_URL
    generate_instagram_profile_page_URL.admin_order_field = 'instagram_user_name'    
    generate_instagram_profile_page_URL.short_description = 'Instagram profile page URL'     
    
    def generate_iconosquare_profile_page_URL(self, p_instagram_user_id):
        '''Generate Iconosquare.com profile page URL for the user
        
        Parameters:
        p_instagram_user_id: Instagram user ID, used to generate URL for profile page
        
        Returns:
        URL of Iconosquare profile page for this GoodUser
        '''
        
        l_iconosquare_profile_page_URL = 'http://iconosquare.com/viewer.php#/user/%s/' % (p_instagram_user_id)
        return l_iconosquare_profile_page_URL  
    generate_iconosquare_profile_page_URL.admin_order_field = 'instagram_user_name'    
    generate_iconosquare_profile_page_URL.short_description = 'Iconosquare profile page URL'  
    
    

    '''Determine what is displayed when GoodUser is displayed as a list'''
    list_display = ('user_name', 'instagram_user_name', 'full_name', 
                    'number_of_followers', 'creation_date', 'last_processed_date', 
                    'to_be_processed' ,'was_added_recently', 'pk')
    
    '''Add fields by which you want to sort a model'''
    ordering = ('user_name',)
    
    prepopulated_fields = {"instagram_user_name": ("user_name",)}
    
    '''Add fields from the model by which we want to filter list'''
    list_filter = ('to_be_processed', 'instagram_user_name_valid', 
                   'last_processed_date', 'creation_date',
                   )
    
    '''Add a field from the model by which you want to search'''
    search_fields = ('instagram_user_name', )
 
    '''Define a list of actions listed in Admin interface Action combo box'''
    actions = (process_gooduser, set_goodusers_process_true, 
               set_goodusers_process_false, analyze_gooduser_find_friends)
    
    filter_horizontal = ('user_category', 'user_attribute', )
    
    '''Determine what is dispalayed on GoodUser Admin Edit form'''
    fieldsets = [
        ('General Information', {'fields': ['user_name', 'full_name', 'email', 
                                            'instagram_user_name'
                                            ]
                                 }
         ),
        ('GoodUser Processing Information', {'fields': ['last_processed_date', 
                                                        'times_processed', 'to_be_processed',
                                                        'last_processed_friends_date',
                                                        'times_processed_for_friends',
                                                        'to_be_processed_for_friends'
                                                        ]
                                             }
         ),         
        ('Instagram Information', {'fields': ['number_of_media', 
                                              'number_of_followers', 'number_of_followings', 
                                              'instagram_user_full_name', 'instagram_profile_picture_URL',
                                              'instagram_user_bio', 'instagram_user_website_URL',
                                              'instagram_user_id', 'instagram_user_name_valid']
                                   }
         ),
                               
        ( 'Categories and Attributes', {'fields': ['user_category', 
                                                        'user_attribute'
                                                        ]
                                             }
         ),
          
        ('Additional Social Media Information', {'fields': ['twitter_handle', 'facebook_handle',
                                                             'eyeem_handle'
                                                             ],
                                                'classes': ['collapse']
                                                }
         ),
        ('Other Web Sites Links for Good User', {'fields': ['instagram_user_profile_page_URL',
                                                            'iconosquare_user_profile_page_URL'
                                                            ]
                                                 }
         ),

        #('Time Information', {'fields': ['creation_date', 'last_update_date']})                 
    ]
    
    
class GoodUserRawAdmin(admin.ModelAdmin):
    '''Definition of Admin interface for GoodUsers model'''
    
    list_display = ('instagram_user_name', 'to_be_processed',
                    'instagram_user_name_valid', 'creation_date',
                    'last_update_date' 
                    )  
    
    '''Add fields from the model by which we want to filter list'''
    list_filter = ('to_be_processed', 'instagram_user_name_valid', 
                   'instagram_user_name_valid', 'creation_date',
                   )
    
    '''Add a field from the model by which you want to search'''
    search_fields = ('instagram_user_name', )  
    
    fieldsets = [
        ('General Information', {'fields': [ 
                                            'instagram_user_name'
                                            ]
                                 }
         ),
        ('GoodUser Processing Information', {'fields': [
                                                        'to_be_processed'
                                                        ]
                                             }
         ),         
              

        ('Categories and Attributes', {'fields': ['category1', 'category2',
                                                  'category3', 'category4',
                                                  'category5',
                                                  'attribute_black_and_white',
                                                  'attribute_color',
                                                  'attribute_hdr',
                                                  'attribute_minimal',
                                                  'attribute_abstract',
                                                  'attribute_heavy_edit',
                                                  'attribute_macro',
                                                  'attribute_retro',
                                                  'attribute_color_splash'          
                                                  ]
                                                 }
         ),                
    ]
       
        
# Register your models here.
admin.site.register(GoodUser, GoodUserAdmin)
admin.site.register(GoodUserRaw, GoodUserRawAdmin)
