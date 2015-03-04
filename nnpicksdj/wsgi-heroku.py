"""
WSGI config for nnpicksdj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
from dj_static import Cling
from whitenoise.django import DjangoWhiteNoise
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nnpicksdj.settings.local")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#application = Cling(get_wsgi_application())
application = DjangoWhiteNoise(application)