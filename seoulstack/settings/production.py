from .base import *

DEBUG = False

ALLOWED_HOSTS = ['188.166.252.161', 'localhost', 'seoulstack.com']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.environ.get('DATABASE_NAME', os.path.join(BASE_DIR, 'db.postgres')),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    }
}
SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
