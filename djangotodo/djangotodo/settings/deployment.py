import dj_database_url
from . import *

DEBUG = False

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS += [
    'pyyyc-todo.herokuapp.com'
]
