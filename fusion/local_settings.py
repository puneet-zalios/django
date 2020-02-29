import cx_Oracle

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': "wrangler",
        'USER': 'fusion',
        'PASSWORD': "secret",
        'HOST': 'wrangler_db',
        'PORT': '5432'
    }
}
