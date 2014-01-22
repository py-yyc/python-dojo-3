from . import *

DATABASES['default'] = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'USER': 'postgres',
    'PASSWORD': 'test',
    'HOST': '127.0.0.1',
    'PORT': '5432',
}
