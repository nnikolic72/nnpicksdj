from django.db import models

# Create your models here.
class Attribute(models.Model):
    '''Provide category functionality'''
    
    def __str__(self):
        '''return text for this class'''
        
        return(self.title)
    
    title = models.CharField(max_length=200, null=False, blank=False, default='')
    description = models.CharField(max_length=200, null=True, blank=True, default='')
    slug = models.SlugField(max_length=50, null=True, blank=True, default='')
    
    class Meta:
        ordering = ('title', )
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'
        