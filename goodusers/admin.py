from django.contrib import admin
from django.utils import timezone
from django.conf import settings
from django.utils.translation import ugettext as _  # @UnusedImport
from django.db.models import Q

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

    def process_gooduser(self, request, queryset):
        '''Action -> Do what is needed to process a GoodUser with Instagram API
           Process only users that are marked to be processed -> to_be_processed==True
        '''
        
        instagram_utils = InstagramUserAdminUtils()
        buf = instagram_utils.process_instagram_user(request, queryset)
        
        
        self.message_user(request, buf)
    process_gooduser.short_description = 'Process Good User by Instagram API' 
    
    
    def set_goodusers_process_true(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected GoodUsers to True.
           Process only GoodUsers that have flag to_be_processed set to False.
           to_be_processed==False
        '''
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_false(request, queryset)
        self.message_user(request, message)
    set_goodusers_process_true.short_description = 'Set "To Be Processed for basic info" to "Yes"' 


    def set_goodusers_process_false(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected GoodUsers to False.
           Process only GoodUsers that have flag to_be_processed set to True.
           to_be_processed==True
        '''
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_true(request, queryset)
        self.message_user(request, message)                
    set_goodusers_process_false.short_description = 'Set "To Be Processed for basic info" to "No"'  
    
      

    '''Determine what is displayed when GoodUser is displayed as a list'''
    list_display = ('instagram_user_name', 
                    'number_of_followers', 'creation_date',
                    'to_be_processed_for_basic_info',
                    'to_be_processed_for_friends', 
                    'to_be_processed_for_followings',
                    'to_be_processed_for_photos',                      
                     'pk'
                    )
    
    '''Which fields are editable in Admin list view'''
    list_editable = (
                    'to_be_processed_for_basic_info',
                    'to_be_processed_for_friends', 
                    'to_be_processed_for_followings',
                    'to_be_processed_for_photos',                        
                     )     
    '''Add fields by which you want to sort a model'''
    ordering = ('instagram_user_name',)
    
    #prepopulated_fields = {"instagram_user_name": ("user_name",)}
    
    '''Add fields from the model by which we want to filter list'''
    list_filter = ('to_be_processed_for_basic_info', 
                   'to_be_processed_for_friends', 
                   'to_be_processed_for_followings',
                   'to_be_processed_for_photos',                  
                   'instagram_user_name_valid', 
                   'creation_date',
   
                   )
    
    '''Add a field from the model by which you want to search'''
    search_fields = ('instagram_user_name', )
    
    readonly_fields = ('user_type',)    
 
    '''Define a list of actions listed in Admin interface Action combo box'''
    actions = (process_gooduser, set_goodusers_process_true, 
               set_goodusers_process_false)
    
    filter_horizontal = ('user_category', 'user_attribute', )
    
    '''Determine what is dispalayed on GoodUser Admin Edit form'''
    fieldsets = [
        ('General Information', {'fields': ['instagram_user_name', 'user_type',
                                            'full_name', 'email', 
                                            
                                            ]
                                 }
         ),
        ('GoodUser Processing Information', {'fields': ['last_processed_for_basic_info_date', 
                                                        'times_processed_for_basic_info', 
                                                        'to_be_processed_for_basic_info',
                                                        
                                                        'last_processed_for_friends_date',
                                                        'times_processed_for_friends',
                                                        'to_be_processed_for_friends',
                                                        
                                                        'last_processed_for_followings_date',
                                                        'times_processed_for_followings',
                                                        'to_be_processed_for_followings',
                                                        
                                                        'last_processed_for_photos_date',
                                                        'times_processed_for_photos',
                                                        'to_be_processed_for_photos'
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
                                            'instagram_user_name',
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
       


        
class InstagramUserAdminUtils():
    '''Helper functions for Instagram users administrations'''
    
    l_find_top_n_photos = None
    l_search_last_photos = None
        
    l_analyzed_followers = 0
    l_found_friends = 0
    l_analyzed_goodusers = 0
    l_private_followers = 0 
    
    l_instagram_api_limit = 0
    l_instagram_api_limit_start = 0
    l_instagram_api_limit_end = 0    
            
    def analyze_instagram_user_find_friends(self, request, obj):
        ''' Analyze Instagram Users followers and find potential
           Friends.
        '''
        
        self.l_analyzed_followers = 0
        self.l_found_friends = 0
        self.l_analyzed_goodusers = 0
        self.l_private_followers = 0 
        self.l_already_friends = 0 
        
        #queryset = queryset.filter(to_be_processed_for_friends=True)
        
        if obj.to_be_processed_for_friends == True:
            ig_session = InstagramSession(p_is_admin=True, p_token='')
            ig_session.init_instagram_API()
            
            self.l_instagram_api_limit_start, self.l_instagram_api_limit = \
                 ig_session.get_api_limits()
            
            #for obj in queryset:
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
                        
                        if settings.TEST_APP == True:
                            '''Override for testing, analyze less followers'''
                            l_analyze_n_followers = settings.TEST_APP_FRIENDS_TR_ANALYZE_N_FRIENDS
                             
                        l_best_instagram_followers = \
                            BestFollowers(l_instagram_user_id, l_analyze_n_followers, ig_session)
                            
                        l_instagram_friends = \
                            l_best_instagram_followers.get_best_instagram_followers()
                        self.l_analyzed_goodusers += 1
                        self.l_analyzed_followers += l_best_instagram_followers.l_analyzed_followers
                        self.l_private_followers += l_best_instagram_followers.l_private_followers
                        self.l_already_friends += l_best_instagram_followers.l_already_friends
                        if l_instagram_friends:
                            '''Found followers - save them to our database'''
                            for follower in l_instagram_friends:
                                l_exists = Friend.objects.filter(instagram_user_id=follower.id)
                                
                                if l_exists.count() == 0:
                                    '''Friend does not exist - add new'''
                                    instagram_utils = InstagramUserAdminUtils()
                                    l_new_friend = \
                                        Friend(instagram_user_id=follower.id,
                                               instagram_user_name=follower.username, instagram_user_name_valid=True,
                                               instagram_user_full_name=follower.full_name,
                                               instagram_profile_picture_URL=follower.profile_picture,
                                               instagram_user_bio=follower.bio,
                                               instagram_user_website_URL=follower.website,
                                               is_user_active=True,
                                               number_of_followers=follower.counts[u'followed_by'],
                                               number_of_followings=follower.counts[u'follows'],
                                               number_of_media=follower.counts[u'media'],
                                               instagram_user_profile_page_URL=instagram_utils.generate_instagram_profile_page_URL(follower.username),
                                               iconosquare_user_profile_page_URL=instagram_utils.generate_iconosquare_profile_page_URL(follower.id)
                                               )
                                    l_new_friend.save()                                        
                                    l_new_friend.gooduser.add(obj)
    
                                    self.l_found_friends += 1
                                else:
                                    '''Friend exists - add new gooduser'''
                                    l_exists.gooduser.add(obj)
                                    l_exists.save()
                                    pass
                
            obj.save()    

        self.l_instagram_api_limit_end, self.l_instagram_api_limit = \
             ig_session.get_api_limits()
             
        buf = 'Analyzed %s Goodusers. Analyzed %s folowers. Found %s private followers.' \
               ' Found %s new Friends (%s existing friends). Instagram API (%s - %s/%s / diff: %s)' \
               % (self.l_analyzed_goodusers, self.l_analyzed_followers,
                  self.l_private_followers, self.l_found_friends, self.l_already_friends,
                  self.l_instagram_api_limit_start, self.l_instagram_api_limit_end, 
                  self.l_instagram_api_limit, 
                  (int(self.l_instagram_api_limit_start) - int(self.l_instagram_api_limit_end))
                  )
        return buf
    analyze_instagram_user_find_friends.short_description = 'Find new friends from GoodUser'         

        
    def analyze_instagram_user(self, api, p_instagram_user):
        '''Do the processing of Good User with Instagram API
           
           Parameters:
           p_gooduser - one GoodUser we want to process
        '''
        buf = None
        
        if api:
            user_search = api.is_instagram_user_valid(p_instagram_user.instagram_user_name)
            
        if user_search:
            buf = 'Success'
            instagram_user = api.get_instagram_user(user_search[0].id)
                
            p_instagram_user.number_of_followers = instagram_user.counts[u'followed_by']
            p_instagram_user.number_of_followings = instagram_user.counts[u'follows']
            p_instagram_user.number_of_media = instagram_user.counts[u'media']
            p_instagram_user.instagram_user_name = instagram_user.username
            p_instagram_user.instagram_user_full_name = instagram_user.full_name
            p_instagram_user.instagram_user_id = instagram_user.id
            p_instagram_user.instagram_profile_picture_URL = instagram_user.profile_picture
            p_instagram_user.instagram_user_bio = instagram_user.bio  
            p_instagram_user.instagram_user_website_URL = instagram_user.website
            p_instagram_user.instagram_user_name_valid = True
        else:
            p_instagram_user.instagram_user_name_valid = False
            buf = "analyze_gooduser: ERR-00008 Could not find user %s on Instagram." % (p_instagram_user.instagram_user_name)
   
               
        return p_instagram_user, buf
        
        
    def process_instagram_user(self, request, queryset):
        '''Do what is needed to process a Instagram User with Instagram API
           Process only users that are marked to be processed -> to_be_processed==True
        '''
        

    
        queryset = queryset.filter(
                       Q(to_be_processed_for_basic_info=True) | \
                       Q(to_be_processed_for_photos=True) | \
                       Q(to_be_processed_for_friends=True) | \
                       Q(to_be_processed_for_followings=True)
                   )
                   
        l_counter_for_basic_info = 0
        l_counter_for_friends = 0
        l_counter_for_followings = 0
        l_counter_pics = 0
        message_basic_info = None
        message_find_friends = None
        message_best_photos = None
        message_followings = None
        
        ig_session = InstagramSession(p_is_admin=True, p_token='')
        ig_session.init_instagram_API()
        
        self.l_instagram_api_limit_start, self.l_instagram_api_limit = \
             ig_session.get_api_limits()
        
        for obj in queryset:
            if obj.to_be_processed_for_basic_info == True:
                obj.to_be_processed_for_basic_info = False
                obj.last_processed_date = timezone.datetime.now()
                obj.times_processed_for_basic_info = obj.times_processed_for_basic_info + 1
                instagram_utils = InstagramUserAdminUtils()
                obj.instagram_user_profile_page_URL = instagram_utils.generate_instagram_profile_page_URL(obj.instagram_user_name)
                obj.iconosquare_user_profile_page_URL = instagram_utils.generate_iconosquare_profile_page_URL(obj.instagram_user_id)
                '''get Instagram user data'''
                obj, message_basic_info = self.analyze_instagram_user(ig_session, obj)
                l_counter_for_basic_info += 1
                obj.save()
            
            '''Analyze photos of this user'''
            if obj.to_be_processed_for_photos == True:
                if obj.user_type == 'gooduser':
                    self.l_find_top_n_photos = settings.GOODUSERS_FIND_TOP_N_PHOTOS
                    self.l_search_last_photos = settings.GOODUSERS_SEARCH_N_PHOTOS
                    
                if obj.user_type == 'friend':
                    self.l_find_top_n_photos = settings.FRIENDS_FIND_TOP_N_PHOTOS
                    self.l_search_last_photos = settings.FRIENDS_SEARCH_N_PHOTOS 
                    
                if obj.user_type == 'member':
                    self.l_find_top_n_photos = settings.MEMBERS_FIND_TOP_N_PHOTOS
                    self.l_search_last_photos = settings.MEMBERS_SEARCH_N_PHOTOS                                                       
                                    
                l_best_photos = BestPhotos(obj.instagram_user_id, self.l_find_top_n_photos, 
                                           self.l_search_last_photos, ig_session
                                           )
                l_best_photos.get_instagram_photos()
                l_top_photos = None
                if l_best_photos.l_user_has_photos:
                    l_best_photos.get_top_photos()
                    l_top_photos = l_best_photos.top_photos_list
                    obj.times_processed_for_photos = obj.times_processed_for_photos + 1
                obj.save()
                
                '''Delete old best photos for this user'''
                if obj.user_type == 'gooduser':
                    Photo.objects.filter(good_user_id=obj.pk).delete()
                if obj.user_type == 'friend':
                    Photo.objects.filter(friend_id=obj.pk).delete()
                if obj.user_type == 'member':
                    Photo.objects.filter(member_id=obj.pk).delete()                    
                
                '''Insert new best photos for this user'''
                if l_top_photos:
                    for val in l_top_photos:
                        if obj.user_type == 'gooduser':                        
                            rec = Photo(instagram_photo_id=val[0], photo_rating=val[1], good_user_id=obj)
                        if obj.user_type == 'friend':                        
                            rec = Photo(instagram_photo_id=val[0], photo_rating=val[1], friend_id=obj)  
                        if obj.user_type == 'member':                        
                            rec = Photo(instagram_photo_id=val[0], photo_rating=val[1], member_id=obj)                                                      
                        rec.save()
                        l_counter_pics += 1
                        
                obj.to_be_processed_for_photos = False
                obj.save()
                message_best_photos = 'Success'                        


            '''Analyze followers of this user for friends'''
            if obj.to_be_processed_for_friends == True:
                message_find_friends = self.analyze_instagram_user_find_friends(request, obj)
                obj.to_be_processed_for_friends = False
                obj.times_processed_for_friends = obj.times_processed_for_friends + 1
                obj.save()
                l_counter_for_friends += 1
            
            '''Analyze followers of this user for followings'''
            if obj.to_be_processed_for_followings == True:
                l_counter_for_followings += 1
                obj.times_processed_for_followings = obj.times_processed_for_followings + 1
                obj.to_be_processed_for_followings = False
                obj.save()
                message_followings = 'Success'                
                pass                                                 
            
            

        self.l_instagram_api_limit_end, self.l_instagram_api_limit = \
             ig_session.get_api_limits()
             

                     

        buf = '%s users processed for basic info (Messages "%s").' \
              ' Processed %s photos (Messages "%s").' \
              ' Processed %s users for friends (Messages "%s").'  \
              ' Processed %s users for followings (Messages: "%s").'  \
              ' Instagram API (%s - %s/%s / diff: %s)' % \
              (l_counter_for_basic_info, message_basic_info, 
               l_counter_pics, message_best_photos, 
               l_counter_for_friends, message_find_friends, 
               l_counter_for_followings, message_followings,             
               self.l_instagram_api_limit_start, self.l_instagram_api_limit_end, 
               self.l_instagram_api_limit, 
               (int(self.l_instagram_api_limit_start) - int(self.l_instagram_api_limit_end))
              )
    
        return buf
        #self.message_user(request, buf)
    process_instagram_user.short_description = 'Process Instagram User by Instagram API' 
    
            
    def set_instagram_users_process_true(self, request, queryset):
          
        queryset = queryset.filter(to_be_processed_for_basic_info=False)
        l_counter = 0
        
        for obj in queryset:
            obj.to_be_processed_for_basic_info = True        
            obj.save()
            l_counter += 1
        
         
        buf = '%s user(s) flagged to "To Be Processed for basic info" successfully.' \
            % (l_counter)
        
        return buf
   
    def set_instagram_users_process_false(self, request, queryset):
          
        queryset = queryset.filter(to_be_processed_for_basic_info=True)
        l_counter = 0
        
        for obj in queryset:
            obj.to_be_processed_for_basic_info = False        
            obj.save()
            l_counter += 1
        
 
        buf = '%s user(s) flagged to "Not To Be Processed for basic info" successfully.' \
            % (l_counter)
        
        return buf   
               
    def generate_instagram_profile_page_URL(self, p_instagram_user_name):
        '''Generate Instagram.com profile page URL for the user
        
        Parameters:
        p_instagram_user_name: Instagram user name, used to generate URL for profile page
        
        Returns:
        URL of Instagram profile page for this GoodUser
        '''
        
        l_instagram_profile_page_URL = 'http://www.instagram.com/%s' % (p_instagram_user_name)
        return l_instagram_profile_page_URL   
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
    generate_iconosquare_profile_page_URL.short_description = 'Iconosquare profile page URL' 

                       
# Register your models here.
admin.site.register(GoodUser, GoodUserAdmin)
admin.site.register(GoodUserRaw, GoodUserRawAdmin)
