import cx_Oracle

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'ORCLCDB',
        'USER': 'sys',
        'PASSWORD': 'Oradoc_db1',
        'HOST': 'wrangler_db',
        'PORT': '1521',
        'OPTIONS': {
            'mode': cx_Oracle.SYSDBA
        },
    }
}
