"""
Example settings for local development

Use this file as a base for your local development settings and copy
it to {{ project_name }}/settings/local.py. It should not be checked into
your code repository.

"""
from blackhatstore.settings.base import *   # pylint: disable=W0614,W0401

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('elujan', 'eduardo.lujan.p@gmail.com'),
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DB_DIR, 'dev.db'),
    }
}

ROOT_URLCONF = 'blackhatstore.urls'
#WSGI_APPLICATION = 'blackhatstore.wsgi.local.application'
