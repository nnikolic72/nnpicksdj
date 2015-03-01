from django.contrib import admin, messages
from django.utils import timezone
from django.utils.translation import ugettext as _  # @UnusedImport

from .models import GoodUser
from photos.models import Photo

from libs.instagram.tools import InstagramSession, BestPhotos


   
class GoodUserAdmin(admin.ModelAdmin):
    '''Definition of Admin interface for GoodUsers model'''                                                          
    
    l_instagram_api_limit = 0
    l_instagram_api_limit_start = 0
    l_instagram_api_limit_end = 0
    
    l_find_top_n_photos = 10
    l_search_last_photos = 500
                                                                        
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
               set_goodusers_process_false)
    
    '''Determine what is dispalayed on GoodUser Admin Edit form'''
    fieldsets = [
        ('General Information', {'fields': ['user_name', 'full_name', 'email', 
                                            'instagram_user_name', 'user_category'
                                            ]
                                 }
         ),
        ('GoodUser Processing Information', {'fields': ['last_processed_date', 
                                                        'times_processed', 'to_be_processed'
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
    
    
# Register your models here.
admin.site.register(GoodUser, GoodUserAdmin)
