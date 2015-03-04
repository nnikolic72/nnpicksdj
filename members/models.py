from django.db import models
from django.contrib.auth.models import User


from goodusers.models import GoodUser
from friends.models import Friend

#from categories.models import Category
#from attributes.models import Attribute
# Create your models here.

from goodusers.models import InstagramUser

class Member(InstagramUser):
    '''Logged user preferences'''
    
    user_type = models.CharField(editable=False, default='member', max_length=50)
        
    #Link to User Django model
    user_id = models.OneToOneField(User, null=False, blank=False)

    # Which Goodusers this Member follows on squaresensor
    goodusers_followings = models.ManyToManyField(GoodUser, null=True, blank=True, through='MemberToGooduser') 
    
    # Which potential Friends this member interacted with or followed on squaresensor
    potential_friends = models.ManyToManyField(Friend, null=True, blank=True, through='MemberToFriend') 
    
    likes_in_last_hour = models.IntegerField(null=True, blank=True, default=0)
    comments_in_last_hour = models.IntegerField(null=True, blank=True, default=0)
        
    paid_member = models.BooleanField(null=False, blank=False, default=False)
    membership_expiry_date = models.DateTimeField(null=True, blank=True)
    
    class Meta(InstagramUser.Meta):
        ordering = ('user_id__username',)
        verbose_name = 'Member'
        verbose_name_plural = 'Members'       
    
    
class MemberToGooduser(models.Model):
    '''Additional ManyToMany fields for relation of Member and Gooduser'''
    
    LOW = 'LOW'
    HIGH = 'HIGH'
    LEVEL_CHOICES = (
                     (LOW, 'Low'),
                     (HIGH, 'High')
                     ) 
    
    member = models.ForeignKey(Member)
    gooduser = models.ForeignKey(GoodUser)
    follow_level = models.CharField(max_length=20, null=True, blank=True, 
                             choices=LEVEL_CHOICES, default=LOW)
    
    # How this Member rates the Gooduser
    rating = models.IntegerField(null=True, blank=True)
    
    # is this GoodUser Member's favorite?
    favorite = models.BooleanField(null=False, blank=False, default=False)
    
    
class MemberToFriend(models.Model):
    '''Additional ManyToMany fields for relation of Member and Friend'''
    
    LOW = 'LOW'
    HIGH = 'HIGH'
    OFF = 'OFF'
    LEVEL_CHOICES = (
                     (LOW, 'Low'),
                     (HIGH, 'High'),
                     (OFF, 'Off'),
                     ) 
    
    member = models.ForeignKey(Member)
    friend = models.ForeignKey(Friend)
    follow_level = models.CharField(max_length=20, null=True, blank=True, 
                             choices=LEVEL_CHOICES, default=LOW)
    
    # How this Member rates the Friend
    rating = models.IntegerField(null=True, blank=True)
    
    # when Member last interacted with Friend
    last_interacted_time = models.DateTimeField(null=True, blank=True)
    
    # did the Friend followed Member?
    interaction_result = models.BooleanField(null=False, blank=False, default=False)
    
    # is this Friend Member's favorite?
    favorite = models.BooleanField(null=False, blank=False, default=False)
       
        