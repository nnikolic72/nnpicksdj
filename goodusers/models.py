from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class GoodUser(models.Model):
    '''Data model class for Good User, handpicked Instagram user'''
    '''Created my first branch and a first change'''
    
    def generate_instagram_profile_page_URL(self):
        '''Generate Instagram.com profile page URL for the user'''
        
        l_instagram_profile_page_URL = ''
        l_instagram_profile_page_URL = 'http://www.instagram.com/%s' % (self.instagram_user_name)
        return l_instagram_profile_page_URL
    
    
    def generate_iconosquare_profile_page_URL(self):
        '''Generate Iconosquare.com profile page URL for the user'''
        
        l_iconosquare_profile_page_URL = ''
        l_iconosquare_profile_page_URL = 'http://iconosquare.com/viewer.php#/user/%s/' % (self.instagram_user_id)
        return l_iconosquare_profile_page_URL    
    
    
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
    instagram_user_id = models.CharField(max_length=100, unique=True, null=True,
                                        blank=True)
    instagram_user_profile_page_URL = models.URLField(max_length=255, null=True, 
                                                    blank=True, default='')
    iconosquare_user_profile_page_URL = models.URLField(max_length=255, null=True, 
                                                    blank=True, default='')
    instagram_profile_picture_URL = models.URLField(max_length=255, null=True, 
                                                    blank=True)
    instagram_user_bio = models.CharField(max_length=500, null=True, blank=True)
    instagram_user_website_URL = models.URLField(max_length=255, null=True, 
                                                 blank=True)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    instagram_user_full_name = models.CharField(max_length=100, null=True, 
                                                blank=True)
    is_user_active = models.BooleanField(default=False, null=False)
    
    number_of_followers = models.IntegerField(default=0, null=True, blank=True)
    number_of_followings = models.IntegerField(default=0, null=True, blank=True)
    number_of_media = models.IntegerField(default=0, null=True, blank=True)
    
    '''Time-stamp when was the last time GoodUser was updated using Instagram API'''
    last_processed_date = models.DateTimeField('GoodUser processed date', null=True, blank=True)
    '''Number of times GoodUser is processed'''
    times_processed = models.IntegerField('Number of times processed', default=0, null=False)
    '''GoodUser is marked for processing next time GoodUser Batch Processing is run'''
    to_be_processed = models.BooleanField(default=True, null=False)
    
    creation_date = models.DateTimeField('GoodUser creation date', auto_now_add=True)
    last_update_date = models.DateTimeField('GoodUser creation date', auto_now=True)
    
class GoodUsersCategories(models.Model):
    '''Link table between users and categories'''
    
    good_user_id = models.IntegerField()
    category_id = models.IntegerField()
