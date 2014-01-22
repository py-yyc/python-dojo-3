import dj_database_url
from . import *

DATABASES['default'] = dj_database_url.config()
