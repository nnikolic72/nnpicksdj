from django.db import models

# Create your models here.
class GoodUser(models.Model):
    '''Data model class for Good User, handpicked Instagram user'''
    
    user_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(null=True)
    twitter_handle = models.CharField(max_length=100, null=True, blank=True)
    facebook_handle = models.CharField(max_length=100, null=True, blank=True)
    eyeem_handle = models.CharField(max_length=100, null=True, blank=True)
    instagram_user_name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100)
    instagram_user_full_name = models.CharField(max_length=100)
    number_of_followers = models.IntegerField(default=0, null=True)
    number_of_followings = models.IntegerField(default=0, null=True)
    number_of_media = models.IntegerField(default=0, null=True)
    creation_date = models.DateTimeField('GoodUser creation date', auto_now_add=True)
    last_update_date = models.DateTimeField('GoodUser creation date', auto_now=True)
    
class GoodUsersCategories(models.Model):
    '''Link table between users and categories'''
    
    good_user_id = models.IntegerField()
    category_id = models.IntegerField()
