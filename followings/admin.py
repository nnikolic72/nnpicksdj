from django.contrib import admin
#from django.conf import settings
#from django.utils import timezone

from .models import Following
#from photos.models import Photo
from goodusers.admin import InstagramUserAdminUtils

#from libs.instagram.tools import InstagramSession, BestPhotos

# Register your models here.
class FollowingAdmin(admin.ModelAdmin):
    '''Definition of Admin interface for Following model'''
    

    def process_following(self, request, queryset):
        '''Action -> Do what is needed to process a Following with Instagram API
           Process only Following that are marked to be processed -> to_be_processed==True
        '''
        
        instagram_utils = InstagramUserAdminUtils()
        buf = instagram_utils.process_instagram_user(request, queryset)

        self.message_user(request, buf)
    process_following.short_description = 'Process Following by Instagram API'        
    
    
    
    def set_followings_process_true(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected Followings to True.
           Process only Followings that have flag to_be_processed set to False.
           to_be_processed==False
        '''
        
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_true(request, queryset)
        self.message_user(request, message)
    set_followings_process_true.short_description = 'Set "To Be Processed for basic info" -> Yes' 


    def set_followings_process_false(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected Followings to False.
           Process only Followings that have flag to_be_processed set to True.
           to_be_processed==True
        '''
        
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_false(request, queryset)
        self.message_user(request, message)
    set_followings_process_false.short_description = 'Set "To Be Processed for basic info" -> No'     
    
    
    
    
    
    
    
    
    def set_followings_process_photos_true(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected GoodUsers to True.
           Process only GoodUsers that have flag to_be_processed set to False.
           to_be_processed==False
        '''
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_photos_true(request, queryset)
        self.message_user(request, message)
    set_followings_process_photos_true.short_description = 'Set "To Be Processed for photos" to "Yes"' 


    def set_followings_process_photos_false(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected GoodUsers to False.
           Process only GoodUsers that have flag to_be_processed set to True.
           to_be_processed==True
        '''
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_photos_false(request, queryset)
        self.message_user(request, message)                
    set_followings_process_photos_false.short_description = 'Set "To Be Processed for photos" to "No"' 
    
           
           
    def set_followings_process_friends_true(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected GoodUsers to True.
           Process only GoodUsers that have flag to_be_processed set to False.
           to_be_processed==False
        '''
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_friends_true(request, queryset)
        self.message_user(request, message)
    set_followings_process_friends_true.short_description = 'Set "To Be Processed for Friends" to "Yes"' 


    def set_followings_process_friends_false(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected GoodUsers to False.
           Process only GoodUsers that have flag to_be_processed set to True.
           to_be_processed==True
        '''
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_friends_false(request, queryset)
        self.message_user(request, message)                
    set_followings_process_friends_false.short_description = 'Set "To Be Processed for Friends" to "No"'            
           
           

    def set_followings_process_followings_true(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected GoodUsers to True.
           Process only GoodUsers that have flag to_be_processed set to False.
           to_be_processed==False
        '''
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_friends_true(request, queryset)
        self.message_user(request, message)
    set_followings_process_followings_true.short_description = 'Set "To Be Processed for Friends" to "Yes"' 


    def set_followings_process_followings_false(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected GoodUsers to False.
           Process only GoodUsers that have flag to_be_processed set to True.
           to_be_processed==True
        '''
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_friends_false(request, queryset)
        self.message_user(request, message)                
    set_followings_process_followings_false.short_description = 'Set "To Be Processed for Friends" to "No"' 
        
        
    list_display = (
                    'instagram_user_name', 
                    'is_user_active', 
                    'followed_by_n_goodusers',
                    'number_of_media',
                     'number_of_followers', 'number_of_followings', 
                     'to_be_processed_for_basic_info', 'to_be_processed_for_photos'
                    )    
    
    list_editable = (
                     'to_be_processed_for_basic_info', 'to_be_processed_for_photos'
                     )
    
    ordering = ('instagram_user_name', 'instagram_user_name', 'is_user_active', )
    
    list_filter = ('to_be_processed_for_basic_info',  
                   'to_be_processed_for_followings',
                   'to_be_processed_for_photos', 
                    'instagram_user_name_valid', 
                    'creation_date',
                   )
    
    search_fields = ('instagram_user_name', )
    
    readonly_fields = ('user_type', 'followed_by_n_goodusers',)    
    
    actions = (process_following, 
               set_followings_process_true, 
               set_followings_process_false,
               set_followings_process_photos_false,
               set_followings_process_photos_true,            
               )    
    
    fieldsets = [
        ('General Information', {'fields': [ 'instagram_user_name', 'user_type'
                                            ]
                                 }
         ),
                 
        ('Source', {'fields': [ 'gooduser'
                               ]
                    }
         ),
        ('Followings Processing Information', {'fields': ['last_processed_for_basic_info_date', 
                                                        'times_processed_for_basic_info', 
                                                        'to_be_processed_for_basic_info',
                                                        
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
        ]
    
# Register your models here.
admin.site.register(Following, FollowingAdmin)   