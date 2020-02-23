# Every setting in base.py can be overloaded by redefining it here.
from .base import *

# Django App Secretkey change if you want
SECRET_KEY = 'REPLACETHISSHIT'

# Change this to change the name of the auth site
SITE_NAME = 'Alliance Auth'

DEBUG = False
# Add any additional apps to this list. Pre-Populated with some Apps
INSTALLED_APPS += [
'allianceauth.services.modules.discord',
'allianceauth.services.modules.mumble',
]

#### ADD YOUR OWN LOCAL DATABASE DETAILS HERE
DATABASES['default'] = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'aauth',
    'USER': 'aauth',
    'PASSWORD': 'PASSWORD',
    'HOST': '127.0.0.1',
    'PORT': '3306',
}


ESI_SSO_CLIENT_ID = ''
ESI_SSO_CLIENT_SECRET = ''
ESI_SSO_CALLBACK_URL = ''


REGISTRATION_VERIFY_EMAIL = False
EMAIL_HOST = ''
EMAIL_PORT = 587
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''
#######################################
# Add any custom settings below here. #
#######################################

ROOT_URLCONF = 'myauth.urls'
WSGI_APPLICATION = 'myauth.wsgi.application'
STATIC_ROOT = "/var/www/myauth/static/"
BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": "redis:6379",
        "OPTIONS": {
            "DB": 1,
        }
    }
}
