from django.db import models

from goodusers.models import GoodUser

# Create your models here.

class Photo(models.Model):
    '''Class model for Photographs'''
    
    instagram_photo_id = models.CharField(max_length=255, null=False)
    instagram_user_id = models.CharField(max_length=100, null=True,
                                        blank=True
                                        )
    instagram_picture_URL = models.URLField(max_length=255, null=True, 
                                                blank=True
                                                )
        
    good_user_id = models.ForeignKey(GoodUser)
    likes = models.IntegerField(default=0, null=True, blank=True)
    comments = models.IntegerField(default=0, null=True, blank=True)
    
    creation_date = models.DateTimeField('GoodUser creation date', auto_now_add=True)
    last_update_date = models.DateTimeField('GoodUser creation date', auto_now=True)    