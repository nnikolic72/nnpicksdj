from django.db import models
from django.utils.translation import ugettext as _
from django.utils import timezone  # @UnusedImport

#from categories.models import Category
from goodusers.models import GoodUser

# Create your models here.

class Friend(models.Model):
    '''Friend model - holds potential friends list'''
    
    def __str__(self):
        '''return text for this class'''
        
        return(self.instagram_user_name) 
    
    '''which goodusers are their "source". We scan GoodUsers followers and insert suitable followers into our
    Friends database. 
    '''
    gooduser = models.ManyToManyField(GoodUser, null=True, blank=True)
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
    instagram_user_full_name = models.CharField(max_length=100, null=True, 
                                                blank=True
                                                )
    
    # is user active in last X days
    is_user_active = models.BooleanField(default=False, null=False)
    
    number_of_followers = models.IntegerField(default=0, null=True, blank=True)
    number_of_followings = models.IntegerField(default=0, null=True, blank=True)
    number_of_media = models.IntegerField(default=0, null=True, blank=True)    
    
    '''Time-stamp when was the last time Friend was updated using Instagram API'''
    last_processed_date = models.DateTimeField('Friend processed date', null=True, blank=True)
    '''Number of times GoodUser is processed'''
    times_processed = models.IntegerField('Number of times processed', default=0, null=False)
    '''Friend is marked for processing next time Friend Batch Processing is run'''
    to_be_processed = models.BooleanField(default=True, null=False,
                                          help_text=_('Check if you want this Friend to be ' 
                                                     'processed in the next Batch Run'
                                                     )
                                          )
    
    # which category their "parent" GoodUsers have
    #friend_category = models.ManyToManyField(Category, null=True, blank=True)
    creation_date = models.DateTimeField('Friend creation date', auto_now_add=True)
    last_update_date = models.DateTimeField('Friend creation date', auto_now=True)
    
    class Meta:
        get_latest_by = 'creation_date'
        ordering = ('instagram_user_name',)
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'        