import os
from datetime import timedelta
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DEV_APPS = [
    'drf_yasg',
]

INSTALLED_APPS += DEV_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DEV_NAME'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
        'CHARSET': 'utf8mb4',
        'COLLATION': 'utf8mb4_general_ci'
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles')
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'config.renderers.CustomRenderer',
    ],
    'ACCESS_TOKEN_LIFETIME': timedelta(days=999),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=999),
}
