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

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

config = RawConfigParser()
config.read(BASE_DIR + '\\settings.ini')

DATABASE_USER = config.get('database', 'DATABASE_USER')
DATABASE_PASSWORD = config.get('database', 'DATABASE_PASSWORD')
DATABASE_HOST = config.get('database', 'DATABASE_HOST')
DATABASE_PORT = config.get('database', 'DATABASE_PORT')
DATABASE_ENGINE = config.get('database', 'DATABASE_ENGINE')
DATABASE_NAME = config.get('database', 'DATABASE_NAME')

INSTAGRAM_API_KEY = config.get('instagram', 'SECRET_KEY')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ae&33=yk5lm9vd*6r*yrxzpng+!pf8^c!z66pofg!y=s49t1ey'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

TEMPLATE_DIRS = [BASE_DIR + '\\templates', BASE_DIR + '\\templates\\admin']

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
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
try:
    from settings_local import DATABASE_ENGINE, DATABASE_NAME, DATABASE_USER, \
                               DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT
    
    #pass
except:
    pass

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': DATABASE_ENGINE,
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

