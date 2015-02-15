from sys import exc_info

from django.contrib import admin, messages
from django.utils import timezone

from instagram import InstagramAPI
from instagram.bind import InstagramAPIError, InstagramClientError

from .models import GoodUser
from nnpicksdj.settings import INSTAGRAM_API_KEY
#from django.conf import settings

    
class GoodUserAdmin(admin.ModelAdmin):
    '''Definition of Admin interface for GoodUsers model'''                                                          
                                                                        
    def init_instagram_API(self, request):
        '''Initializes Instagram API session
        
        Parameters: -
        Returns: Instagram API session
        '''
        
        '''Read variable from settings.py'''
        #INSTAGRAM_API_KEY = getattr(settings, 'INSTAGRAM_API_KEY')
        access_token = INSTAGRAM_API_KEY
        try:
            api = InstagramAPI(access_token=access_token)
        except InstagramAPIError as e:
            buf = None
            buf = "process_gooduser: ERR-00001 Instagram API Error %s : %s" % (e.status_code, e.error_message)
            self.message_user(request, buf, level=messages.WARNING)
            return None
        except InstagramClientError as e:
            buf = None
            buf = "process_gooduser: ERR-00002 Instagram Client Error %s : %s" % (e.status_code, e.error_message)
            self.message_user(request, buf, level=messages.WARNING)
            return None
        except:
            buf = None
            buf = "process_gooduser: ERR-00003 Unexpected error: " + exc_info()[0]    
            self.message_user(request, buf, level=messages.ERROR)
            raise  
        
        return api        
        
    
    def analyze_gooduser(self, request, api, p_gooduser):
        '''Do the processing of Good User with Instagram API
           
           Parameters:
           p_gooduser - one GoodUser we want to process
        '''
        try:
            user_search = api.user_search(q=p_gooduser.instagram_user_name, count=1)
        except InstagramAPIError as e:
            buf = None
            buf = "analyze_gooduser: ERR-00004 Instagram API Error %s : %s" % (e.status_code, e.error_message)
            self.message_user(request, buf, level=messages.WARNING)
            return None
        except InstagramClientError as e:
            buf = None
            buf = "analyze_gooduser: ERR-00005 Instagram Client Error %s : %s" % (e.status_code, e.error_message)
            self.message_user(request, buf, level=messages.WARNING)
            return None
        except:
            buf = None
            buf = "analyze_gooduser: ERR-00006 Unexpected error: " + exc_info()[0]    
            self.message_user(request, buf, level=messages.ERROR)
            raise          
        
        instagram_user = api.user(user_search[0].id)
        p_gooduser.number_of_followers = instagram_user.counts[u'followed_by']
        p_gooduser.number_of_followings = instagram_user.counts[u'follows']
        p_gooduser.number_of_media = instagram_user.counts[u'media']
        p_gooduser.instagram_user_name = instagram_user.username
        p_gooduser.instagram_user_full_name = instagram_user.full_name
        p_gooduser.instagram_user_id = instagram_user.id
        p_gooduser.instagram_profile_picture_URL = instagram_user.profile_picture
        p_gooduser.instagram_user_bio = instagram_user.bio  
        p_gooduser.instagram_user_website_URL = instagram_user.website
               
        return p_gooduser    
    
    
    def process_gooduser(self, request, queryset):
        '''Action -> Do what is needed to process a GoodUser with Instagram API
           Process only users that are marked to be processed -> to_be_processed==True
        '''
        
        queryset = queryset.filter(to_be_processed=True)
        l_counter = 0
        
        api = self.init_instagram_API(request)
        
        for obj in queryset:
            obj.to_be_processed = False
            obj.last_processed_date = timezone.datetime.now()
            obj.times_processed = obj.times_processed + 1
            obj.instagram_user_profile_page_URL = self.generate_instagram_profile_page_URL(obj.instagram_user_name)
            obj.iconosquare_user_profile_page_URL = self.generate_iconosquare_profile_page_URL(obj.instagram_user_id)
            obj = self.analyze_gooduser(request, api, obj)
            obj.save()
            l_counter += 1
        
        self.message_user(request, '%s user(s) processed successfully.' % (l_counter))
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
    
    '''Add fields from the model by which we want to filter list'''
    list_filter = ('to_be_processed', 'last_processed_date', 'creation_date')
    
    '''Add a field from the model by which you want to search'''
    search_fields = ('instagram_user_name', )
 
    '''Define a list of actions listed in Admin interface Action combo box'''
    actions = (process_gooduser, set_goodusers_process_true, 
               set_goodusers_process_false)
    
    '''Determine what is dispalayed on GoodUser Admin Edit form'''
    fieldsets = [
        ('General Information', {'fields': ['user_name', 'full_name', 'email', 
                                            'instagram_user_name'
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
                                              'instagram_user_id']
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