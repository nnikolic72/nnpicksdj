'''
Created on Mar 6, 2015

@author: n.nikolic
'''

from django.conf.urls import patterns, url

from .views import (
                    FollowingsListView, FollowingsDetailView
                    )

urlpatterns = patterns('', 
                       url(r'^$', FollowingsListView.as_view(
                                                             page_template='followings/index_page.html'
                                                             ), name = 'index'
                           ),
                       url(r'^(?P<p_instagram_user_name>.+)/$', FollowingsDetailView.as_view(), 
                           name='details'
                           ),                       
                       )