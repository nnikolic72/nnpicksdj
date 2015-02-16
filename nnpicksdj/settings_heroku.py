"""
Django settings for nnpicksdj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from ConfigParser import RawConfigParser
from django.conf.global_settings import TEMPLATE_DIRS
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), r"settings.ini"))


DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite')
}
#DATABASES['default'] =  dj_database_url.config()



INSTAGRAM_API_KEY = config.get('instagram', 'SECRET_KEY')
#INSTAGRAM_API_KEY = '1546646729.2d6fe64.91d6953b286d467ea889016903648d96'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ae&33=yk5lm9vd*6r*yrxzpng+!pf8^c!z66pofg!y=s49t1ey'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

TEMPLATE_DIRS = [BASE_DIR + '/nnpicksdj/templates/nnpicksdj', 
                 BASE_DIR + '/templates', 
                 BASE_DIR + '/templates/admin', 
                 ]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'goodusers'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'nnpicksdj.urls'

WSGI_APPLICATION = 'nnpicksdj.wsgi.application'

'''Load settings_local.py from top-level project directory if present. 
   Used to override settings on the project level.
   Everyone can use this file as a local-only file, without pushing to remote
   repository.
'''


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


