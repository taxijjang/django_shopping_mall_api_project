import os
from datetime import timedelta
from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DEV_APPS = [
    'django_seed',
]

INSTALLED_APPS += DEV_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DEV_NAME'),
        'USER': os.environ.get('DB_USER'),
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

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis_service:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': [
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ],
#     'DEFAULT_PAGINATION_CLASS': 'core.paginations.CustomPagination',
#     'PAGE_SIZE': 10,
#     'ACCESS_TOKEN_LIFETIME': timedelta(days=999),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=999),
# }

# SWAGGER_SETTINGS = {
#     'SECURITY_DEFINITIONS': {
#         'api_key': {
#             'type': 'apiKey',
#             'description': 'Personal API Key authorization',
#             'in': 'header',
#             'name': 'Authorization'
#         }
#     },
#     'DEFAULT_AUTO_SCHEMA_CLASS': 'core.schemas.CustomAutoSchema',
#     # 'DEFAULT_MODEL_RENDERING': 'example',
# }

# CELERY SETTINGS
CELERY_TIMEZONE = 'Asia/Seoul'
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
# CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['json', 'yaml']
CELERY_RESULT_BACKEND = 'django-db'

RABBITMQ_USER = os.environ.get('RABBITMQ_USER', 'guest')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD', 'guest')
RABBITMQ_QUEUE_EXPIRES = 300.0
RABBITMQ_MESSAGE_EXPIRES = RABBITMQ_QUEUE_EXPIRES
