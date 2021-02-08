from .base import *

DEBUG = False

ALLOWED_HOSTS = ['188.166.252.161', 'localhost']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('S_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('S_DATABASE', 'sstack_prod'),
        'USER': os.environ.get('S_USER', 'sstackadmin'),
        'PASSWORD': os.environ.get('S_PASSWORD', 'simonlee1979'),
        'HOST': os.environ.get('S_HOST', 'localhost'),
        'PORT': os.environ.get('S_PORT', ''),
    }
}
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True