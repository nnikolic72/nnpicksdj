from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, RedirectView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nnpicksdj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^goodusers/', include('goodusers.urls', namespace='goodusers') ),
    url(r'^photos/', include('photos.urls', namespace='photos') ),
    url(r'^login/', include('iguserauth.urls', namespace='login') ),
    #url(r'^logout/', login_required( TemplateView.as_view(template_name="index.html")), name='apphome'),
    url(r'', include('social_auth.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='apphome'),
)
