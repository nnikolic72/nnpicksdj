from django.db import models

'''
class IGUserManager(models.Manager):
    def create_user(self, username, email):
        return self.model._default_manager.create(username=username)

# Create your models here.
class IGUserAuth(models.Model):
    #Instgaram user authentication model - used to process IG user as local
    userid = models.CharField(max_length=128, blank=True, null=True)
    username = models.CharField(max_length=128, blank=True, null=True)
    access_token = models.CharField(max_length=256, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = IGUserManager()

    def is_authenticated(self):
        return True
'''            