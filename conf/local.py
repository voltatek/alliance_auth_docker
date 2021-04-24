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
    'HOST': 'auth_mysql',
    'PORT': '3306',
}

# Register an application at https://developers.eveonline.com for Authentication
# & API Access and fill out these settings. Be sure to set the callback URL
# to https://example.com/sso/callback substituting your domain for example.com
# Logging in to auth requires the publicData scope (can be overridden through the
# LOGIN_TOKEN_SCOPES setting). Other apps may require more (see their docs).

ESI_SSO_CLIENT_ID = ''
ESI_SSO_CLIENT_SECRET = ''
ESI_SSO_CALLBACK_URL = ''
ESI_USER_CONTACT_EMAIL = ''    # A server maintainer that CCP can contact in case of issues.


# By default emails are validated before new users can log in.
# It's recommended to use a free service like SparkPost or Elastic Email to send email.
# https://www.sparkpost.com/docs/integrations/django/
# https://elasticemail.com/resources/settings/smtp-api/
# Set the default from email to something like 'noreply@example.com'
# Email validation can be turned off by uncommenting the line below. This can break some services.
# REGISTRATION_VERIFY_EMAIL = False
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
