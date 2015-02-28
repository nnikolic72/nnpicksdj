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
import os
import re
from unipath import Path

from ConfigParser import ConfigParser  # @UnusedImport
#from django.conf.global_settings import TEMPLATE_DIRS

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = Path(__file__).ancestor(3)
BASE_DIR = PROJECT_DIR.child('nnpicksdj')

'''
TEMPLATE_DIRS = [BASE_DIR + '\\..\\nnpicksdj\\templates\\nnpicksdj', 
                 BASE_DIR + '\\..\\templates', 
                 BASE_DIR + '\\..\\templates\\admin', 
                 ]
'''

TEMPLATE_DIRS = (PROJECT_DIR.child("nnpicksdj").child("templates").child("nnpicksdj"),)


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
#    'csvimport',  # use AppConfig for django >=1.7 csvimport >=2.2
    'import_export',
    'dajaxice',
    'goodusers',
    'photos',
    'iguserauth',
    'categories',
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
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login/error/'



'''
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'iguserauth.pipeline.redirect_to_form',
    'iguserauth.pipeline.username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'social_auth.backends.pipeline.misc.save_status_to_session',
    'iguserauth.pipeline.redirect_to_form2',
    'iguserauth.pipeline.first_name',
)
'''

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
#STATIC = BASE_DIR + '/static/'
#STATIC_ROOT = BASE_DIR + '/static/'

#STATIC_ROOT = os.path.join(BASE_DIR,'static')


