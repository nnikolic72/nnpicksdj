import datetime
from django.db import models
from django.utils.translation import ugettext as _

from goodusers.models import GoodUser

# Create your models here.

class Photo(models.Model):
    '''Class model for Photographs'''
    
    def admin_thumbnail(self):
        '''Function to show thumbnail of instagram photo in Admin interface'''
        
        if hasattr(self, 'instagram_thumbnail_URL'):
            return u'<a href="%s"><img src="%s"></a>' % \
                   (self.instagram_link_URL, self.instagram_thumbnail_URL)
    admin_thumbnail.short_description = _('Thumbnail')
    admin_thumbnail.allow_tags = True

    instagram_photo_id = models.CharField(max_length=255, null=False)
    instagram_low_resolution_URL = models.URLField(max_length=255, null=True, 
                                                blank=True
                                                )
    instagram_thumbnail_URL = models.URLField(max_length=255, null=True, 
                                                blank=True
                                                )
    instagram_standard_resolution_URL = models.URLField(max_length=255, null=True, 
                                                blank=True
                                                )
    instagram_link_URL = models.URLField(max_length=255, null=True, 
                                                blank=True
                                                )
    instagram_caption = models.TextField(max_length=1000, null=True, blank=True)
    instagram_tags = models.TextField(max_length=1000, null=True, blank=True)
    instagram_created_time = models.CharField(max_length=100, null=True, blank=True)
    instagram_photo_valid = models.BooleanField(default=True, null=False, blank=True)
               
    good_user_id = models.ForeignKey(GoodUser, null=True)
    instagram_likes = models.IntegerField(default=0, null=True, blank=True)
    instagram_comments = models.IntegerField(default=0, null=True, blank=True)
    
    creation_date = models.DateTimeField('Photo creation date', auto_now_add=True,
                                         default=datetime.datetime.now())
    last_update_date = models.DateTimeField('Photo last update date', auto_now=True,
                                            default=datetime.datetime.now())    