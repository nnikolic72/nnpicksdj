from django.conf.urls import patterns, url

'''Import views.py module from goodusers app'''
#from .views import index, detail
from goodusers import views

urlpatterns = patterns('', 
                       url(r'^$', views.IndexView.as_view(), name = 'index'),
                       url(r'^(?P<p_instagram_user_name>.+)/$', views.detail, 
                           name='details'
                           )
                       )