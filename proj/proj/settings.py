"""
Django settings for proj project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kr$sxdcpuk3qggkmz'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True

ALLOWED_HOSTS = ['localhost', u'127.0.0.1']



# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'home',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'proj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proj.wsgi.application'


# !!!!!!!!!!--set djcelery
import djcelery

djcelery.setup_loader()

# rabbitmq server address
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
# store task results in rabbitmq
CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost:5672//'
# task result life time until they will be deleted
CELERY_TASK_RESULT_EXPIRES = 7*86400  # 7 days
# needed for worker monitoring
CELERY_SEND_EVENTS = True

# where to store periodic tasks (needed for scheduler)
CELERYBEAT_SCHEDULER = "djcelery.schedulers.DatabaseScheduler"
##########

# --Enables error emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CELERY_SEND_TASK_ERROR_EMAILS = True
SERVER_EMAIL='test@gmail.com'
#CELERY_DEFAULT_RATE_LIMIT = 10

# Name and email addresses of recipients
ADMINS = (
    ('test', 'chenjun@deepforestmedia.com'),
)

# use gmial setting
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='test@gmail.com'
# unlock google capcha https://accounts.google.com/b/2/DisplayUnlockCaptcha
# add app password in gmail https://myaccount.google.com/u/1/security
EMAIL_HOST_PASSWORD='dfxyax' 
EMAIL_PORT=587
EMAIL_USE_TLS =True


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

'''DATABASES = {
    'default': { #default is local db 
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}'''
DATABASES = {
    
    'default': { 
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'celerytestproj',                     
        'USER': 'name',
        'PASSWORD': '123',
        'HOST': '123',                 
        'PORT': '3306', 
    }
}
#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

# Django settings for proj project.

#DEBUG = True
#TEMPLATE_DEBUG = DEBUG

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'US/Pacific'#'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

