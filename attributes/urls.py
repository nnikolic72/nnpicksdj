'''
Created on Mar 3, 2015

@author: n.nikolic
'''
from django.conf.urls import patterns, url

from categories import views

urlpatterns = patterns('', 
                       url(r'^$', views.IndexView.as_view() , name = 'index'),
                       url(r'^(?P<p_attribute_name>.+)/$', views.detail, 
                           name='details'
                           )                       
                       )