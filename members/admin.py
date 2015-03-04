from django.contrib import admin

from goodusers.admin import InstagramUserAdminUtils
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    def process_member(self, request, queryset):
        '''Action -> Do what is needed to process a Members with Instagram API
           Process only Members that are marked to be processed -> to_be_processed==True
        '''
        
        instagram_utils = InstagramUserAdminUtils()
        buf = instagram_utils.process_instagram_user(request, queryset)
        
        
        self.message_user(request, buf)
    process_member.short_description = 'Process Members by Instagram API' 
    
    
    def set_members_process_true(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected Members to True.
           Process only Members that have flag to_be_processed set to False.
           to_be_processed==False
        '''
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_false(request, queryset)
        self.message_user(request, message)
    set_members_process_true.short_description = 'Set "To Be Processed for basic info" to "Yes"' 


    def set_members_process_false(self, request, queryset):
        '''Action -> Set "to_be_processed" flag for selected Members to False.
           Process only Members that have flag to_be_processed set to True.
           to_be_processed==True
        '''
        admin_utils = InstagramUserAdminUtils()
        message = admin_utils.set_instagram_users_process_true(request, queryset)
        self.message_user(request, message)                
    set_members_process_false.short_description = 'Set "To Be Processed for basic info" to "No"'  
    
      

    '''Determine what is displayed when GoodUser is displayed as a list'''
    list_display = ('user_id', 'instagram_user_name', 'paid_member',
                    'membership_expiry_date', 
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
    list_filter = ('paid_member',
                   'to_be_processed_for_basic_info', 
                   'to_be_processed_for_friends', 
                   'to_be_processed_for_followings',
                   'to_be_processed_for_photos',                  
                   'instagram_user_name_valid', 
                   'creation_date',
                   'membership_expiry_date',
   
                   )
    
    '''Add a field from the model by which you want to search'''
    search_fields = ('instagram_user_name', )
    
    readonly_fields = ('user_type',)    
 
    '''Define a list of actions listed in Admin interface Action combo box'''
    actions = (process_member, set_members_process_true, 
               set_members_process_false)
    
    filter_horizontal = ('user_category', 'user_attribute', )
    
    '''Determine what is displayed on member Admin Edit form'''
    fieldsets = [
        ('General Information', {'fields': ['user_id', 'instagram_user_name', 'user_type',
                                            'full_name', 'email', 
                                            
                                            ]
                                 }
         ),
        ('Membeship Information', {'fields': ['paid_member', 'membership_expiry_date'
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
    
admin.site.register(Member, MemberAdmin)    