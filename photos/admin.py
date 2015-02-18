from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Photo
from libs.instagram.tools import InstagramSession

# Register your models here.
class PhotoAdmin(admin.ModelAdmin):
    '''Photos model Admin definition'''
    
    def get_instagram_photo_info(self, api, p_photo):
        '''Retrieves information about on Instagram photo
        
        Parameters:
        api - Instagram session object
        p_photo - source Photo object
        Returns - object filled with Instagram photo information
        '''
        
        l_photo = api.get_instagram_photo_info(p_photo.instagram_photo_id)
        
        if l_photo:
            p_photo.instagram_photo_valid = True
            p_photo.instagram_photo_id = l_photo.id
            p_photo.instagram_low_resolution_URL = \
                l_photo.get_low_resolution_url()
            p_photo.instagram_thumbnail_URL = l_photo.get_thumbnail_url()
            p_photo.instagram_standard_resolution_URL = \
                l_photo.get_standard_resolution_url()
            p_photo.instagram_link_URL = l_photo.link
            p_photo.instagram_caption = l_photo.caption
            #p_photo.instagram_tags = ','.join(l_photo.tags)
            p_photo.instagram_created_time = l_photo.created_time
            p_photo.instagram_likes = l_photo.like_count
            p_photo.instagram_comments = l_photo.comment_count
        else:
            p_photo.instagram_photo_valid = False
            
        return p_photo
        
    
    def process_photos_by_instagram_api(self, request, queryset):
        '''Action -> process photos by Instagram API'''
        
        ig_session = InstagramSession()
        ig_session.init_instagram_API()
        
        self.l_instagram_api_limit_start, self.l_instagram_api_limit = \
             ig_session.get_api_limits()    
    
        l_counter = 0
        
        for obj in queryset:
            obj = self.get_instagram_photo_info(ig_session, obj)
            obj.save()
            l_counter += 1
            
            
        self.l_instagram_api_limit_end, self.l_instagram_api_limit = \
             ig_session.get_api_limits()
                     
        if l_counter == 1:
            buf = '1 photo processed successfully. Instagram API (%s - %s/%s)' % \
                    (self.l_instagram_api_limit_start, self.l_instagram_api_limit_end, 
                     self.l_instagram_api_limit
                     )
        else:
            buf = '%s photos processed successfully.  Instagram API (%s - %s/%s)' % \
                    (l_counter, self.l_instagram_api_limit_start, self.l_instagram_api_limit_end, 
                     self.l_instagram_api_limit
                     )    
        self.message_user(request, buf)
    process_photos_by_instagram_api.short_description = 'Process photos by Instagram API'        
            
    list_display = ('instagram_photo_id', 'good_user_id', 'admin_thumbnail', )
    
    fieldsets = [
        ('General Information', {'fields': ['instagram_photo_id', 
                                            'good_user_id',
                                            'instagram_caption',
                                            'instagram_tags',
                                            'instagram_photo_valid'
                                            ]
                                 }
         ),
        ('Instagram Stats', {'fields': ['instagram_likes', 'instagram_comments'
                                        ]
                             }
         ),
        ('Date and time information', {'fields': ['instagram_created_time'
                                                  ]
                                       }
         )
    ]
    
    actions = (process_photos_by_instagram_api, )
    
admin.site.register(Photo, PhotoAdmin)