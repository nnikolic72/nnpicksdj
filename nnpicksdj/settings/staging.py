'''
Created on Feb 28, 2015

@author: tanja
'''

import dj_database_url
from memcacheify import memcacheify  # @UnresolvedImport

#insert into requirements.txt:
#
#django-heroku-memcacheify==0.8
#pylibmc==1.2.3
CACHES = memcacheify()

from nnpicksdj.settings.base import * # @UnusedWildImport

# HEROKU SETUP
# heroku config:set DJANGO_SETTINGS_MODULE=nnpicksdj.settings.staging
#
# git add .
# git commit -m "my app"
# git push heroku master
# heroku run python manage.py migrate

# heroku pg:info # vraca informacije o statusu postgres baze na Heroku (koliko redova je ostalo)

config = ConfigParser()
settings_path = PROJECT_DIR.child('nnpicksdj').child("settings")
settings_path = Path(settings_path, 'settings.ini')
config.read(settings_path)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Heroku part
DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite')
}
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
ALLOWED_HOSTS = ['*']
MIDDLEWARE_CLASSES += ('django.middleware.clickjacking.XFrameOptionsMiddleware',)

INSTAGRAM_API_KEY = config.get('instagram', 'SECRET_KEY')
INSTAGRAM_CLIENT_ID = config.get('instagram', 'CLIENT_ID')
INSTAGRAM_CLIENT_SECRET = config.get('instagram', 'CLIENT_SECRET')

SECRET_KEY =  config.get('nnpicksdj', 'SECRET_KEY')

DEBUG = False

TEMPLATE_DEBUG = False


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}