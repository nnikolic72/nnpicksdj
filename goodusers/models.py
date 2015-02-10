from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class GoodUser(models.Model):
    '''Data model class for Good User, handpicked Instagram user'''
    
    
    def __str__(self):
        '''return text for this class'''
        
        return(self.user_name)
    
    def was_added_recently(self):
        '''Was the good user added from yesterday until now'''
         
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)
        
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(null=True)
    twitter_handle = models.CharField(max_length=100, null=True, blank=True)
    facebook_handle = models.CharField(max_length=100, null=True, blank=True)
    eyeem_handle = models.CharField(max_length=100, null=True, blank=True)
    instagram_user_name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    instagram_user_full_name = models.CharField(max_length=100, null=True, blank=True)
    number_of_followers = models.IntegerField(default=0, null=True)
    number_of_followings = models.IntegerField(default=0, null=True)
    number_of_media = models.IntegerField(default=0, null=True)
    creation_date = models.DateTimeField('GoodUser creation date', auto_now_add=True)
    last_update_date = models.DateTimeField('GoodUser creation date', auto_now=True)
    
class GoodUsersCategories(models.Model):
    '''Link table between users and categories'''
    
    good_user_id = models.IntegerField()
    category_id = models.IntegerField()
