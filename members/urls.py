'''
Created on Mar 1, 2015

@author: tanja
'''
from django.conf.urls import patterns, url
#from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from .views import ( 
                    DashboardIndexView, 
                    FeedView, 
                    MyBestPhotosView
                    )

urlpatterns = patterns('', 
    url(r'^$', login_required(DashboardIndexView.as_view()), name='index'),
    url(r'^feed/$', login_required(FeedView.as_view()), name='feed'),
    url(r'^mybest/$', login_required(MyBestPhotosView.as_view()), name='mybest'),    
    )