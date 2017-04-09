"""Base settings shared by all environments"""
# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *   # pylint: disable=W0614,W0401

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'UTC'
USE_TZ = True
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', 'English'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a2ho&-531glg#alli2!b$!9+##kr+__256j*31xb40h$a&uyz#'

INSTALLED_APPS = (
    'blackhatstore.apps.authentication',
    #'south',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
)

#==============================================================================
# Calculation of directories relative to the project module location
#==============================================================================

import os
import sys
import blackhatstore as project_module

PYTHON_BIN = os.path.dirname(sys.executable)
# Assume that the presence of 'activate_this.py' in the python bin/
# directory means that we're running in a virtual environment.

# Add the project dir to the python path
PROJECT_DIR, PROJECT_MODULE_NAME = os.path.split(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
if not PROJECT_DIR in sys.path:
  sys.path.insert(0, PROJECT_DIR)
ve_path = os.path.dirname(os.path.dirname(os.path.dirname(PROJECT_DIR)))

# Add the 'wis' dir to the python path
MODULE_DIR = os.path.join(PROJECT_DIR, PROJECT_MODULE_NAME)
if not MODULE_DIR in sys.path:
  sys.path.insert(1, MODULE_DIR)

# Add the 'apps' dir to the python path
APPS_DIR = os.path.join(MODULE_DIR, 'apps')
if not APPS_DIR in sys.path:
  sys.path.insert(2, APPS_DIR)

# Add the 'lib' dir to the python path
LIB_DIR = os.path.join(MODULE_DIR, 'lib')
if not LIB_DIR in sys.path:
  sys.path.insert(3, LIB_DIR)

# Add the 'lib' dir to the python path
DB_DIR = os.path.join(MODULE_DIR, 'db')
if not DB_DIR in sys.path:
  sys.path.insert(4, DB_DIR)
if not os.path.exists(DB_DIR):
    os.mkdir(DB_DIR)

VAR_ROOT = os.path.join(MODULE_DIR, 'var')

if not os.path.exists(VAR_ROOT):
    os.mkdir(VAR_ROOT)

#==============================================================================
# Project URLS and media settings
#==============================================================================

ROOT_URLCONF = 'blackhatstore.urls'

LOGIN_URL = '/login/'
LOGOUT_URL = '/logout/'
LOGIN_REDIRECT_URL = '/'

STATIC_URL = '/static/'
MEDIA_URL = '/uploads/'

#STATIC_ROOT = os.path.join(MODULE_DIR, 'static')
MEDIA_ROOT = os.path.join(MODULE_DIR, 'uploads')


STATICFILES_DIRS = (
    os.path.join(MODULE_DIR, 'static'),
)

#==============================================================================
# Templates
#==============================================================================

TEMPLATE_DIRS = (
    os.path.join(MODULE_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS += (
)

#==============================================================================
# Middleware
#==============================================================================

MIDDLEWARE_CLASSES += (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

#==============================================================================
# Auth / security
#==============================================================================

AUTHENTICATION_BACKENDS += (
)

#==============================================================================
# Miscellaneous project settings
#==============================================================================

#==============================================================================
# Third party app settings
#==============================================================================


AUTH_USER_MODEL = 'authentication.User'
