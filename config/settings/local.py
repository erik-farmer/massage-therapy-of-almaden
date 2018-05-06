from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7uo&j16ifisaih8*4ylexh((xaf2)8)a#35fz^586&l$0$&w^%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dev_db',
        'USER': 'dev_user',
        'PASSWORD': 'dev_password',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "mtoa"
    }
}

DEFENDER_REDIS_URL = "redis://localhost:6379/0"