from .base import *
import secrets


DEBUG = False


SECRET_KEY = secrets.token_urlsafe(50)

# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
