'''
Created on Feb 23, 2015

@author: n.nikolic
'''

from django.conf.urls import patterns, url

'''Import views.py module from photos app'''
#from .views import index, detail
import views

urlpatterns = patterns('', 
                       url(r'^$', views.home, name = 'login'),
                       url(r'^done/$', views.done, name='done'),
                       url(r'^index/$', views.index, name='index'), 
                       url(r'^ig/$', views.ig, name='ig'),
#                       url(r'^logout/$', views.logout, name='logout'),
                       )