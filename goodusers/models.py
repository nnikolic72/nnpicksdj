import datetime

from django.db import models
from django.utils import timezone
#from django import forms
from django.utils.translation import ugettext as _

from categories.models import Category
from attributes.models import Attribute
#from pip.cmdoptions import editable

class InstagramUser(models.Model):
    '''Abstract base class for GoodUsers, Members, Friends and Followings'''
  
    def __str__(self):
        '''return text for this class'''
    
        return(self.instagram_user_name)
    
    def was_added_recently(self):
        '''Was the good user added from yesterday until now'''
         
        return self.creation_date >= timezone.now() - datetime.timedelta(days=1)
    was_added_recently.admin_order_field = 'creation_date'
    was_added_recently.boolean = True
    was_added_recently.short_description = 'Added recently?'


    email = models.EmailField(null=True, blank=True)
    twitter_handle = models.CharField(max_length=100, null=True, blank=True)
    facebook_handle = models.CharField(max_length=100, null=True, blank=True)
    eyeem_handle = models.CharField(max_length=100, null=True, blank=True)
    instagram_user_name = models.CharField(max_length=100, unique=True)
    instagram_user_name_valid = models.BooleanField(default=True, null=False,
                                          help_text=_('Check if Instagram user is valid/exists.')
                                          )
    instagram_user_id = models.CharField(max_length=100, unique=True, null=True,
                                        blank=True
                                        )
    instagram_user_profile_page_URL = models.URLField(max_length=255, null=True, 
                                                    blank=True, default=''
                                                    )
    iconosquare_user_profile_page_URL = models.URLField(max_length=255, null=True, 
                                                    blank=True, default=''
                                                    )
    instagram_profile_picture_URL = models.URLField(max_length=255, null=True, 
                                                    blank=True
                                                    )
    instagram_user_bio = models.TextField(max_length=500, null=True, blank=True, 
                                          
                                          )
    instagram_user_website_URL = models.URLField(max_length=255, null=True, 
                                                 blank=True
                                                 )
    full_name = models.CharField(max_length=100, null=True, 
                                 blank=True
                                 )
    instagram_user_full_name = models.CharField(max_length=100, null=True, 
                                                blank=True
                                                )
    is_user_active = models.BooleanField(default=False, null=False)
    
    number_of_followers = models.IntegerField(default=0, null=True, blank=True)
    number_of_followings = models.IntegerField(default=0, null=True, blank=True)
    number_of_media = models.IntegerField(default=0, null=True, blank=True)


    '''Number of times Instagram user is processed for basic info'''
    times_processed_for_basic_info = models.IntegerField(
                                        'Number of times Instagram user was processed for basic info', 
                                        default=0, null=False
                                        )
    '''Time-stamp when was the last time GoodUser was processed for Friends using Instagram API'''
    last_processed_for_basic_info_date = models.DateTimeField(
                                             'Instagram user processed date for basic info', 
                                             null=True, blank=True
                                             )   
    '''GoodUser is marked for processing next time GoodUser Batch Processing is run'''
    to_be_processed_for_basic_info = models.BooleanField(verbose_name='TBP Basic Info', default=True, null=False,
                                          help_text=_('Check if you want this Instagram user to be ' 
                                                     'processed in the next Batch Run'
                                                     )
                                          )     
            
            

   
    '''Time-stamp when was the last time Instagram user was processed for Friends using Instagram API'''
    last_processed_for_friends_date = models.DateTimeField('Instagram user processed for friends date', 
                                                       null=True, blank=True
                                                       )    
    '''Number of times Instagram user is processed for friends'''
    times_processed_for_friends = models.IntegerField(
                                        'Number of times Instagram user was processed for friends', 
                                        default=0, null=False
                                        )    
    '''GoodUser is marked for processing for friends next time Instagram user Batch Processing is run'''
    to_be_processed_for_friends = models.BooleanField(verbose_name='TBP Friends', default=False, null=False,
                                          help_text=_('Check if you want this Instagram user to be ' 
                                                     'processed for friends in the next Batch Run'
                                                     )
                                          ) 
    
    
        
    '''Time-stamp when was the last time Instagram user was processed for Followings using Instagram API'''
    last_processed_for_followings_date = models.DateTimeField('Instagram user processed for Followings date', 
                                                       null=True, blank=True
                                                       )    
    '''Number of times Instagram user is processed for friends'''
    times_processed_for_followings = models.IntegerField(
                                        'Number of times Instagram user was processed for Followings', 
                                        default=0, null=False
                                        )    
    '''GoodUser is marked for processing for Followings next time Instagram user Batch Processing is run'''
    to_be_processed_for_followings = models.BooleanField(verbose_name='TBP Followings', 
                                                         default=True, null=False,
                                          help_text=_('Check if you want this Instagram user to be ' 
                                                     'processed for Followings in the next Batch Run'
                                                     )
                                          )     
    
    '''Time-stamp when was the last time Instagram user was processed for Photos using Instagram API'''
    last_processed_for_photos_date = models.DateTimeField('Instagram user processed for Photos date', 
                                                       null=True, blank=True
                                                       )    
    '''Number of times Instagram user is processed for friends'''
    times_processed_for_photos = models.IntegerField(
                                        'Number of times Instagram user was processed for Photos', 
                                        default=0, null=False
                                        )    
    '''GoodUser is marked for processing for Photos next time Instagram user Batch Processing is run'''
    to_be_processed_for_photos = models.BooleanField(verbose_name='TBP Photos', 
                                                     default=True, null=False,
                                          help_text=_('Check if you want this Instagram user to be ' 
                                                     'processed for Photos in the next Batch Run'
                                                     )
                                          )         

    user_category = models.ManyToManyField(Category, null=True, blank=True)
    user_attribute = models.ManyToManyField(Attribute, null=True, blank=True)
    creation_date = models.DateTimeField('GoodUser creation date', auto_now_add=True)
    last_update_date = models.DateTimeField('GoodUser creation date', auto_now=True)
                    
    class Meta:
        abstract = True 
        get_latest_by = 'creation_date'
        ordering = ('instagram_user_name',)           


# Create your models here.
class GoodUser(InstagramUser):
    '''Data model class for Good User, handpicked Instagram user'''
    '''Created my first branch and a first change'''
        
    user_type = models.CharField(editable=False, default='gooduser', max_length=50)
    class Meta(InstagramUser.Meta):
        verbose_name = 'Good User'
        verbose_name_plural = 'Good Users'
    

class GoodUserRaw(models.Model):
    '''Class for import of CSV data. Import a text file into this model and run Action
       "Process RAW data to GoodUser
    '''

    def __str__(self):
        '''return text for this class'''
        
        return(self.instagram_user_name)
        
    instagram_user_name = models.CharField(max_length=100, null=False, blank=False)
    category1 = models.CharField(max_length=100, null=True, blank=True)   
    category2 = models.CharField(max_length=100, null=True, blank=True) 
    category3 = models.CharField(max_length=100, null=True, blank=True) 
    category4 = models.CharField(max_length=100, null=True, blank=True) 
    category5 = models.CharField(max_length=100, null=True, blank=True)   
    attribute_black_and_white = models.CharField(max_length=100, null=True, blank=True)
    attribute_color = models.CharField(max_length=100, null=True, blank=True)
    attribute_hdr = models.CharField(max_length=100, null=True, blank=True)
    attribute_minimal = models.CharField(max_length=100, null=True, blank=True)
    attribute_abstract = models.CharField(max_length=100, null=True, blank=True)
    attribute_heavy_edit = models.CharField(max_length=100, null=True, blank=True)
    attribute_macro = models.CharField(max_length=100, null=True, blank=True)
    attribute_retro = models.CharField(max_length=100, null=True, blank=True)
    attribute_color_splash = models.CharField(max_length=100, null=True, blank=True)
    
    instagram_user_name_valid = models.BooleanField(default=True, null=False,
                                          help_text=_('Check if Instagram user is valid/exists.')
                                          )    
    to_be_processed = models.BooleanField(default=True, null=False,
                                          help_text=_('Check if you want this Good User to be ' 
                                                     'processed in the next Batch Run'
                                                     )
                                          )    
    creation_date = models.DateTimeField('GoodUserRaw creation date', auto_now_add=True)
    last_update_date = models.DateTimeField('GoodUserRaw creation date', auto_now=True)    
    
    class Meta:
        get_latest_by = 'creation_date'
        ordering = ('instagram_user_name',)
        verbose_name = 'Good User Raw'
        verbose_name_plural = 'Good Users Raw'
    