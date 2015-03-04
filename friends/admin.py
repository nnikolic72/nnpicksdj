from django.contrib import admin
#from django.conf import settings
#from django.utils import timezone

from .models import Friend
#from photos.models import Photo
from goodusers.admin import InstagramUserAdminUtils

#from libs.instagram.tools import InstagramSession, BestPhotos

# Register your models here.
class FriendAdmin(admin.ModelAdmin):
    '''Definition of Admin interface for Friend model'''
    

    def process_friend(self, request, queryset):
        '''Action -> Do what is needed to process a Friend with Instagram API
           Process only Friends that are marked to be processed -> to_be_processed==True
        '''
        
        instagram_utils = InstagramUserAdminUtils()
        buf = instagram_utils.process_instagram_user(request, queryset)

        self.message_user(request, buf)
    process_friend.short_description = 'Process Friend by Instagram API'        
    
    
    
    def set_friends_process_true(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected Friends to True.
           Process only Friends that have flag to_be_processed set to False.
           to_be_processed==False
        '''
        
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_true(request, queryset)
        self.message_user(request, message)
    set_friends_process_true.short_description = 'Set "To Be Processed for basic info" -> Yes' 


    def set_friends_process_false(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected Friends to False.
           Process only Friends that have flag to_be_processed set to True.
           to_be_processed==True
        '''
        
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_false(request, queryset)
        self.message_user(request, message)
    set_friends_process_false.short_description = 'Set "To Be Processed for basic info" -> No'     
    
    
        
    list_display = (
                    'instagram_user_name', 'is_user_active', 'number_of_media',
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
    
    readonly_fields = ('user_type',)    
    
    actions = (process_friend, 
               set_friends_process_true, 
               set_friends_process_false)    
    
    fieldsets = [
        ('General Information', {'fields': [ 'instagram_user_name', 'user_type'
                                            ]
                                 }
         ),
                 
        ('Source', {'fields': [ 'gooduser'
                               ]
                    }
         ),
        ('Friend Processing Information', {'fields': ['last_processed_for_basic_info_date', 
                                                        'times_processed_for_basic_info', 
                                                        'to_be_processed_for_basic_info',
                                                        
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
        ]
    
# Register your models here.
admin.site.register(Friend, FriendAdmin)       