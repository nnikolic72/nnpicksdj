from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

'''Import views.py module from goodusers app'''
#from .views import index, detail
from goodusers import views

urlpatterns = patterns('', 
                       #url(r'^$', login_required( views.IndexView.as_view() ), name = 'index'),
                       url(r'^$', login_required( views.GoodUsersListView.as_view() ), name = 'index'),
                       url(r'^users/(?P<p_category_name>.+)/$', views.UsersInCategory.as_view(), 
                           name='users_in_category'
                           ),                       
                       url(r'^(?P<p_instagram_user_name>.+)/$', views.GoodUsersDetailView.as_view(), 
                           name='details'
                           ),

                       )