# Django settings for reporting project.
import os

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.pardir))
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

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

ROOT_URLCONF = 'fusion.urls'


TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates').replace('\\','/'),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIRS],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
            ],
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'fusion.incidents',
)

EMAIL_HOST = '10.10.100.6'

try:
    from .local_settings import *
except ImportError:
    pass

# Static files (CSS, JavaScript, Images)

STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "fusion", "images"),
    os.path.join(PROJECT_ROOT, "fusion", "icons"),
    os.path.join(PROJECT_ROOT, "fusion", "scripts"),
    os.path.join(PROJECT_ROOT, "fusion", "styles"),
]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATIC_URL = '/static/'
