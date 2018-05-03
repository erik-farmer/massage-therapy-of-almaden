from .base import *


# Set Security Key via heroku cli
# CREATING SECURE KEYS:
"""
import secrets
secrets.token_urlsafe(some_length)
"""
# heroku config:set SECRET_KEY=somethingstrong


# Configure Django App for Heroku.
import django_heroku
django_heroku.settings(locals())
