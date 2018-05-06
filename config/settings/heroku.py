from .base import *
import secrets
import os

DEBUG = False
REDIS_URL = os.environ.get('REDIS_URL')


SECRET_KEY = secrets.token_urlsafe(50)

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

DEFENDER_REDIS_URL = REDIS_URL

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
