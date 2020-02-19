# Django settings for reporting project.
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BASE_DIR = 'D:/django'

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'RWW',
        'USER': 'fus',
        'PASSWORD': 'FUS',
        'HOST': 'eds1',   # Or an IP Address that your DB is hosted on
        'PORT': '1571'
    }
}

#DATABASE_ENGINE = 'django.db.backends.oracle'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
#DATABASE_NAME = 'RC1W'             # Or path to database file if using sqlite3.
#DATABASE_USER = 'fusion'             # Not used with sqlite3.
#DATABASE_PASSWORD = 'FUSION'         # Not used with sqlite3.
#DATABASE_HOST = 'edb111'             # Set to empty string for localhost. Not used with sqlite3.
#DATABASE_PORT = '1571'             # Set to empty string for default. Not used with sqlite3.

# CACHE
CACHE_BACKEND = 'file://C:/tmp/'


# Local time zone for this installation. Choices can be found here:
# http://www.postgresql.org/docs/8.1/static/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
# although not all variations may be possible on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT.
# Example: "http://media.lawrence.com"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'p6!&o$3k43()qv9ik44m*-y1-6pn_792^&k1eoj!*2awz&(bi7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    #'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.filesystem.Loader',
    #'django.template.loaders.app_directories.load_template_source',
	'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
)
ROOT_URLCONF = 'fusion.urls'

TEMPLATE_DIRS = (
    'D:/django/templates',
    'D:/django/templates/incidents',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',

    'endless_pagination',
    'fusion.incidents',
)

EMAIL_HOST = '10.10.100.6'

try:
    from .local_settings import *
except ImportError:
    pass


STATIC_JS_ROOT = BASE_DIR + '/fusion/script'
STATIC_CSS_ROOT = BASE_DIR + '/fusion/style'
STATIC_IMAGES_ROOT = BASE_DIR + '/fusion/images'
STATIC_ICONS_ROOT = BASE_DIR + '/fusion/icons'
