from django.db import models
from django.utils.translation import ugettext as _  # @UnusedImport
from django.utils import timezone  # @UnusedImport

#from categories.models import Category
from goodusers.models import (
                              InstagramUser,
                              GoodUser
                              )
from members.models import Member

# Create your models here.

class Following(InstagramUser):
    '''Following model - holds potential friends list'''
       
    '''which goodusers are their "source". We scan GoodUsers followings and insert suitable followings into our
    Followings database. 
    '''
    

    
        
    def followed_by_n_goodusers(self):
        '''How many goodusers follow this Following'''
        gooduser_count = self.gooduser.count()
        
        return gooduser_count
    #followed_by_n_goodusers.admin_order_field = 'gooduser__count'
    #followed_by_n_goodusers.boolean = True
    followed_by_n_goodusers.short_description = '# of GoodUsers'
            
    gooduser = models.ManyToManyField(GoodUser, null=True, blank=True)
    member = models.ManyToManyField(Member, null=True, blank=True)
    user_type = models.CharField(editable=False, default='following', max_length=50)
    
    class Meta(InstagramUser.Meta):
        verbose_name = 'Following'
        verbose_name_plural = 'Followings'        
        
    