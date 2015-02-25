'''
Created on Feb 25, 2015

@author: n.nikolic
'''
#from django.views.generic import TemplateView
from django.conf.urls import patterns, url

from categories import views

urlpatterns = patterns('', 
                       url(r'^$', views.IndexView.as_view() , name = 'index'),
                       )