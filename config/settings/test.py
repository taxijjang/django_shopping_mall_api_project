import os

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DEV_APPS = [
    'drf_yasg',
]

INSTALLED_APPS += DEV_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
ROOT_DIR = os.path.dirname(BASE_DIR)

STATIC_URL = '/static/'
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    STATIC_DIR,
]
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
