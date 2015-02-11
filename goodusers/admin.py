from sys import exc_info

from django.contrib import admin, messages
from goodusers.models import GoodUser
from django.utils import timezone

from instagram import InstagramAPI
from instagram.bind import InstagramAPIError, InstagramClientError



    
class GoodUserAdmin(admin.ModelAdmin):
    '''Definition of Admin interface for GoodUsers model'''
    
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
        except InstagramClientError as e:
            buf = None
            buf = "analyze_gooduser: ERR-00005 Instagram Client Error %s : %s" % (e.status_code, e.error_message)
            self.message_user(request, buf, level=messages.WARNING)
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
        '''Do what is needed to process a GoodUser'''
        
        queryset = queryset.filter(to_be_processed=True)
        l_counter = 0
        
        '''ToDo : add this to secret sessions'''
        access_token='1546646729.2d6fe64.91d6953b286d467ea889016903648d96'
        try:
            api = InstagramAPI(access_token=access_token)
        except InstagramAPIError as e:
            buf = None
            buf = "process_gooduser: ERR-00001 Instagram API Error %s : %s" % (e.status_code, e.error_message)
            self.message_user(request, buf, level=messages.WARNING)
        except InstagramClientError as e:
            buf = None
            buf = "process_gooduser: ERR-00002 Instagram Client Error %s : %s" % (e.status_code, e.error_message)
            self.message_user(request, buf, level=messages.WARNING)
        except:
            buf = None
            buf = "process_gooduser: ERR-00003 Unexpected error: " + exc_info()[0]    
            self.message_user(request, buf, level=messages.ERROR)
            raise    
        
        for obj in queryset:
            obj.to_be_processed = False
            obj.last_processed_date = timezone.datetime.now()
            obj.times_processed = obj.times_processed + 1
            obj = self.analyze_gooduser(request, api, obj)
            obj.save()
            l_counter += 1
        
        self.message_user(request, '%s user(s) processed successfully.' % (l_counter))
    process_gooduser.short_description = 'Process Good User by Instagram API' 


    '''Determine what is displayed when GoodUser is displayed as a list'''
    list_display = ('user_name', 'instagram_user_name', 'full_name', 
                    'number_of_followers', 'creation_date', 'last_processed_date', 
                    'to_be_processed' ,'was_added_recently', 'pk')
    
    ordering = ('user_name',)
 
    actions = (process_gooduser,)
    
    '''Determine what is dispalayed on GoodUser Admin Edit form'''
    fieldsets = [
        ('General Information', {'fields': ['user_name', 'full_name', 'email']}),
        ('Instagram Information', {'fields': ['instagram_user_name', 'number_of_media', 
                                              'number_of_followers', 'number_of_followings', 
                                              'instagram_user_full_name', 'instagram_profile_picture_URL',
                                              'instagram_user_bio', 'instagram_user_website_URL',
                                              'instagram_user_id']}),
        ('GoodUser Processing Information', {'fields': ['last_processed_date', 
                                                        'times_processed', 'to_be_processed']}),                 
        ('Additional Social Media Information', {'fields': ['twitter_handle', 'facebook_handle',
                                                             'eyeem_handle'],
                                                'classes': ['collapse']}),

        #('Time Information', {'fields': ['creation_date', 'last_update_date']})                 
    ]
    
    
# Register your models here.
admin.site.register(GoodUser, GoodUserAdmin)