#import datetime
from django.db import models
from django.utils.translation import ugettext as _

from goodusers.models import GoodUser
from friends.models import Friend

from categories.models import Category
from attributes.models import Attribute
from members.models import Member
from followings.models import Following
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
    instagram_photo_processed = models.BooleanField(default=False, null=False, blank=True)
    photo_rating = models.DecimalField(null=True, blank=True, default = 0, max_digits=9,
                                       decimal_places = 2,
                                       help_text='Photo rating relative to users other photos'
                                       )
               
    good_user_id = models.ForeignKey(GoodUser, null=True, blank=True)
    friend_id = models.ForeignKey(Friend, null=True, blank=True)
    member_id = models.ForeignKey(Member, null=True, blank=True)
    following_id = models.ForeignKey(Following, null=True, blank=True)
    
    photo_category = models.ManyToManyField(Category, null=True, blank=True)
    photo_attribute = models.ManyToManyField(Attribute, null=True, blank=True)    
    
    instagram_likes = models.IntegerField(default=0, null=True, blank=True)
    instagram_comments = models.IntegerField(default=0, null=True, blank=True)
    '''Time-stamp when was the last time Photo  was updated using Instagram API'''
    last_processed_date = models.DateTimeField('Photo processed date', null=True, blank=True)
    
    creation_date = models.DateTimeField('Photo creation date', auto_now_add=True,
                                         )
    last_update_date = models.DateTimeField('Photo last update date', auto_now=True,
                                            )    