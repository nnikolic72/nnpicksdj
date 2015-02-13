from django.conf.urls import patterns, url

'''Import views.py module from goodusers app'''
from .views import index, detail

urlpatterns = patterns('', 
                       url(r'^$', index, name = 'index'),
                       url(r'^(?P<p_instagram_user_name>.+)/$', detail, name='details')
                       )