from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nnpicksdj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^goodusers/', include('goodusers.urls')),
    url(r'^photos/', include('photos.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='apphome')
)
