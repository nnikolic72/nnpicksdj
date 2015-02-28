'''
Created on Feb 28, 2015

@author: tanja
'''


from nnpicksdj.settings.old import * # @UnusedWildImport

config = ConfigParser()
try:
    config.read(BASE_DIR + '\\settings\\settings.ini')
    #config.read(BASE_DIR + 'settings.ini')
except:
    raise

DATABASE_USER = config.get('database', 'DATABASE_USER')
DATABASE_PASSWORD = config.get('database', 'DATABASE_PASSWORD')
DATABASE_HOST = config.get('database', 'DATABASE_HOST')
DATABASE_PORT = config.get('database', 'DATABASE_PORT')
DATABASE_ENGINE = config.get('database', 'DATABASE_ENGINE')
DATABASE_NAME = config.get('database', 'DATABASE_NAME')
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databasess
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

INSTAGRAM_CLIENT_ID = config.get('instagram', 'CLIENT_ID')
INSTAGRAM_CLIENT_SECRET = config.get('instagram', 'CLIENT_SECRET')
INSTAGRAM_API_KEY = config.get('instagram', 'SECRET_KEY')

SECRET_KEY =  config.get('nnpicksdj', 'SECRET_KEY')

DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

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

INSTALLED_APPS += ("debug_toolbar", )
INTERNAL_IPS = ("127.0.0.1",)
MIDDLEWARE_CLASSES += \
("debug_toolbar.middleware.DebugToolbarMiddleware", )




