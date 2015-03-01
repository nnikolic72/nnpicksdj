from django.db import models
from django.contrib.auth.models import User

from categories.models import Category
from goodusers.models import GoodUser

# Create your models here.

class dashboard_configuration(models.Model):
    '''Logged user preferences'''
    
    user_id = models.OneToOneField(User, null=False, blank=False)
    user_category = models.ManyToManyField(Category, null=True, blank=True)
    goodusers_followings_high = models.ManyToManyField(GoodUser, null=True, blank=True) 

    
    likes_in_last_hour = models.IntegerField(null=True, blank=True, default=0)
    comments_in_last_hour = models.IntegerField(null=True, blank=True, default=0)
        
    '''Time-stamp when was the last time User was updated using Instagram API'''
    last_processed_date = models.DateTimeField('Dashboard user processed date', null=True, blank=True)
        
    last_update_date = models.DateTimeField('GoodUser creation date', auto_now=True)
    creation_date = models.DateTimeField('GoodUser creation date', auto_now_add=True)
    
    
class MemberToGooduser(models.Model):
    '''Additional ManyToMany fields for relation of Member and Gooduser'''
    
    LOW = 'LOW'
    HIGH = 'HIGH'
    LEVEL_CHOICES = (
                     (LOW, 'Low'),
                     (HIGH, 'High')
                     ) 
    level = models.CharField(maxlength=10, null=True, blank=True, 
                             choices=LEVEL_CHOICES, default=LOW)
    rating = models.IntegerField(null=True, blank=True)
        