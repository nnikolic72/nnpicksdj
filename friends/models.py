from django.db import models
from django.utils.translation import ugettext as _  # @UnusedImport
from django.utils import timezone  # @UnusedImport

#from categories.models import Category
from goodusers.models import (
                              InstagramUser,
                              GoodUser
                              )

# Create your models here.

class Friend(InstagramUser):
    '''Friend model - holds potential friends list'''
       
    '''which goodusers are their "source". We scan GoodUsers followers and insert suitable followers into our
    Friends database. 
    '''
    gooduser = models.ManyToManyField(GoodUser, null=True, blank=True)
    user_type = models.CharField(editable=False, default='friend', max_length=50)
    
    class Meta(InstagramUser.Meta):
        verbose_name = 'Friend'
        verbose_name_plural = 'Friends'        
        
        