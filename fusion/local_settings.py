# import cx_Oracle
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': "wrangler",
#         'USER': 'fusion',
#         'PASSWORD': "secret",
#         'HOST': 'wrangler_db',
#         'PORT': '5432'
#     }
# }
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                            os.pardir))

APP_NAME = 'fusion'
LOG_DIR = PROJECT_ROOT
LOG_FILENAME = '%s.log' % (APP_NAME)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(asctime)s] %(levelname)s [%(module)s:%(funcName)s:'
                      '%(lineno)s %(processName)s %(process)d] %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s:%(funcName)s:%(lineno)s::'
                      '%(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join("%s" % (LOG_DIR), "%s" % (LOG_FILENAME))
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': []
        }
    },
    'loggers': {
        '': {
            'handlers': ['mail_admins', 'console'],
            'level': 'DEBUG',
        },
        'amqp': {
            'handlers': ['mail_admins', 'console'],
            'level': 'INFO'
        },
        'django': {
            'handlers': ['mail_admins', 'console'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins', 'console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False
        },
        'django.db.backends': {
            'handlers': ['mail_admins', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'fusion': {
            'handlers': ['mail_admins', 'console'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}
