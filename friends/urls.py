'''
Created on Mar 2, 2015

@author: n.nikolic
'''

from django.conf.urls import patterns, url

from .views import (
                    FriendsListView, FriendsDetailView
                    )

urlpatterns = patterns('', 
                       url(r'^$', FriendsListView.as_view(), name = 'index'),
                       url(r'^(?P<p_instagram_user_name>.+)/$', FriendsDetailView.as_view(), 
                           name='details'
                           ),                       
                       )