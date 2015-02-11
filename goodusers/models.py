from django.db import models
from django.utils import timezone
import datetime
from django.template.defaultfilters import default

# Create your models here.
class GoodUser(models.Model):
    '''Data model class for Good User, handpicked Instagram user'''
    '''Test GitHub from home PC, second try'''
    
    def xyz(self):
        return None
    
    def __str__(self):
        '''return text for this class'''
        
        return(self.user_name)
    
    def was_added_recently(self):
        '''Was the good user added from yesterday until now'''
         
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)
    was_added_recently.admin_order_field = 'creation_date'
    was_added_recently.boolean = True
    was_added_recently.short_description = 'Added recently?'    
        
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(null=True, blank=True)
    twitter_handle = models.CharField(max_length=100, null=True, blank=True)
    facebook_handle = models.CharField(max_length=100, null=True, blank=True)
    eyeem_handle = models.CharField(max_length=100, null=True, blank=True)
    instagram_user_name = models.CharField(max_length=100, unique=True)
    instagram_user_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    instagram_profile_picture_URL = models.CharField(max_length=255, null=True, blank=True)
    instagram_user_bio = models.CharField(max_length=500, null=True, blank=True)
    instagram_user_website_URL = models.CharField(max_length=255, null=True, blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    instagram_user_full_name = models.CharField(max_length=100, null=True, blank=True)
    
    number_of_followers = models.IntegerField(default=0, null=True, blank=True)
    number_of_followings = models.IntegerField(default=0, null=True, blank=True)
    number_of_media = models.IntegerField(default=0, null=True, blank=True)
    
    '''Time-stamp when was the last time GoodUser was updated using Instagram API'''
    last_processed_date = models.DateTimeField('GoodUser processed date', null=True, blank=True)
    '''Number of times GoodUser is processed'''
    times_processed = models.IntegerField('Number of times processed', default=0, null=False)
    '''GoodUser is marked for processing next time GoodUser Batch Processing is run'''
    to_be_processed = models.BooleanField(default=False, null=False)
    
    creation_date = models.DateTimeField('GoodUser creation date', auto_now_add=True)
    last_update_date = models.DateTimeField('GoodUser creation date', auto_now=True)
    
class GoodUsersCategories(models.Model):
    '''Link table between users and categories'''
    
    good_user_id = models.IntegerField()
    category_id = models.IntegerField()
