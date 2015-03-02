from django.conf.urls import patterns, include, url
from django.contrib import admin
#from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from dajaxice.core import dajaxice_autodiscover, dajaxice_config

dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nnpicksdj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^goodusers/', include('goodusers.urls', namespace='goodusers') ),
    url(r'^friends/', include('friends.urls', namespace='friends') ),
    url(r'^categories/', include('categories.urls', namespace='categories') ),
    url(r'^photos/', include('photos.urls', namespace='photos') ),
    url(r'^members/', include('members.urls', namespace='members') ),
    url(r'^login/', include('iguserauth.urls', namespace='login') ),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'', include('social_auth.urls')),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='apphome'),
)

urlpatterns += staticfiles_urlpatterns()
