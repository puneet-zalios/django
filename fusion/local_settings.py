BASE_DIR = 'D:/django'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'RC1W',
        'USER': 'fusion',
        'PASSWORD': 'FUSION',
        'HOST': 'edb111',
        'PORT': '1571'
    }
}

TEMPLATE_DIRS = (
    'D:/django/templates',
    'D:/django/templates/incidents',
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)