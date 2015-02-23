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
                       url(r'^error/$', views.error, name='error'),
                       url(r'^form/$', views.form, name='form'),
                       url(r'^form2/$', views.form2, name='form2'),                       
#                       url(r'^logout/$', views.logout, name='logout'),
                       )