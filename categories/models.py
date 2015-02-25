from django.db import models

# Create your models here.
class Category(models.Model):
    '''Provide category functionality'''
    
    title = models.CharField(max_length=200, null=False, blank=False, default='')
    description = models.CharField(max_length=200, null=True, blank=True, default='')
    slug = models.CharField(max_length=50, null=True, blank=True, default='')
    parent = models.ForeignKey('self')
    app = models.CharField(max_length=20, null=True, blank=True, default='')