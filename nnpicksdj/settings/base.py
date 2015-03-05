'''
Created on Feb 28, 2015

@author: tanja
'''
#from django.conf.global_settings import SECRET_KEY
"""
Django settings for nnpicksdj project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#import os
import re
from unipath import Path

from ConfigParser import ConfigParser  # @UnusedImport
#from django.conf.global_settings import TEMPLATE_DIRS

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = Path(__file__).ancestor(3)
BASE_DIR = PROJECT_DIR.child('nnpicksdj')

TEMPLATE_DIRS = (PROJECT_DIR.child("nnpicksdj").child("templates").child("nnpicksdj"),
                 )


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    "django.core.context_processors.static",
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_auth',
    'csvimport',  # use AppConfig for django >=1.7 csvimport >=2.2
    'dajaxice',
    'goodusers',
    'friends',    
    'photos',
    'iguserauth',
    'categories',
    'attributes',
    'members',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.contrib.instagram.InstagramBackend',
    'django.contrib.auth.backends.ModelBackend',                      
)



INSTAGRAM_AUTH_EXTRA_ARGUMENTS = {'scope': 'likes comments relationships'}

LOGIN_URL          = '/login/'
LOGIN_REDIRECT_URL = '/members/'
LOGIN_ERROR_URL    = '/login/error/'




SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    #'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'nnpicksdj.pipeline.add_member',     
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages'
)

ROOT_URLCONF = 'nnpicksdj.urls'

WSGI_APPLICATION = 'nnpicksdj.wsgi.application'

IGNORABLE_404_URLS = (
    re.compile(r'^/apple-touch-icon.*\.png$'),
    re.compile(r'^/favicon\.ico$'),
    re.compile(r'^/robots\.txt$'),
)

'''Load settings_local.py from top-level project directory if present. 
   Used to override settings on the project level.
   Everyone can use this file as a local-only file, without pushing to remote
   repository.
'''
#try:
#    from settings_local import DATABASE_ENGINE, DATABASE_NAME, DATABASE_USER, \
#                               DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT
    
    #pass
#except:
#    pass



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
MEDIA_ROOT = PROJECT_DIR.child("media")
STATIC_ROOT = PROJECT_DIR.child("static")
STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, "..//static"),
    PROJECT_DIR.child("assets"),
)
 
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

STATIC_URL = '/static/'


TEST_APP = False
# DAJAX
#DAJAXICE_MEDIA_PREFIX = "dajaxice"
DAJAXICE_DEBUG = True


# APP settings: goodusers
GOODUSERS_FIND_TOP_N_PHOTOS = 10 # how may best photos to find
GOODUSERS_SEARCH_N_PHOTOS = 500 # how many last photos to search while finding the best ones

# APP settings: friends
FRIENDS_FIND_TOP_N_PHOTOS = 5 # how may best photos to find
FRIENDS_SEARCH_N_PHOTOS = 100 # how many last photos to search while finding the best ones

# APP settings: members
MEMBERS_FIND_TOP_N_PHOTOS = 20 # how may best photos to find
MEMBERS_SEARCH_N_PHOTOS = 1000 # how many last photos to search while finding the best ones

# Friends inclusion thresholds
FRIENDS_TR_ANALYZE_N_FRIENDS = 1000
FRIENDS_TR_LAST_POST_BEFORE_DAYS = 2
FRIENDS_TR_MIN_MEDIA_COUNT = 50
FRIENDS_TR_MAX_MEDIA_COUNT = float("inf")
FRIENDS_TR_MIN_FOLLOWINGS = 100
FRIENDS_TR_MAX_FOLLOWINGS = 900
FRIENDS_TR_MIN_FOLLOWERS = 200
FRIENDS_TR_MAX_FOLLOWERS = 800
FRIENDS_TR_MIN_FF_RATIO = 0.85
FRIENDS_TR_MAX_FF_RATIO = 4

#General threshold - when to stop processing Instagram requests
INSTAGRAM_API_THRESHOLD = 500
