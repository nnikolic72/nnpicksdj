from django.conf.urls import patterns, url

'''Import views.py module from photos app'''
#from .views import index, detail
import views

urlpatterns = patterns('', 
                       url(r'^$', views.IndexView.as_view(), name = 'index'),
                       )