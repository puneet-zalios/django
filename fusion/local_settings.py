BASE_DIR = 'D:/django'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'fusion',
        'USER': 'sys',
        'PASSWORD': 'Oradoc_db1',
        'HOST': 'wrangler_db',
        'PORT': '1521'
    }
}

TEMPLATE_DIRS = (
    'D:/django/templates',
    'D:/django/templates/incidents',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)
