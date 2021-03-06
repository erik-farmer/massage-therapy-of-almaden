from .base import *
import secrets
import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}

DEBUG = False
REDIS_URL = os.environ.get('REDIS_URL')
DEFENDER_REDIS_URL = REDIS_URL
SECRET_KEY = os.getenv('SECRET_KEY')

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_URL,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "mtoa"
    }
}

SECURE_SSL_REDIRECT = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_COOKIE_SECURE = True
ALLOWED_HOSTS = ['.herokuapp.com']
