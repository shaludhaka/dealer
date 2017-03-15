"""
Django settings for dealer_rating project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

import djcelery
djcelery.setup_loader()

#LOGIN_URL = '/'
LOGIN_REDIRECT_URL = 'dashboard'
SITE_ID = 1

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wgcyhrmx+-2o=8-y$f27a3twp5^y$%wp^dlv1z^@26u0mwsd0%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'sitebase',
    'djcelery'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'dealer_rating.urls'

WSGI_APPLICATION = 'dealer_rating.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Primary_Dalmia',
        'USER': 'root',
        #'PASSWORD': 'root@123',
        'HOST': 'localhost',  # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = None

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '..', 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media/')
MEDIA_URL = '/media/'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.static',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
)

# Dealer Database Credentials
D_HOST = '127.0.0.1'
D_PORT = '3306'
D_DB = 'Primary_Dalmia'
D_USERNAME = 'root'
#D_PASSWORD = 'root@123'

CELERY_RESULT_BACKEND='amqp'
CELERY_TASK_RESULT_EXPIRES=18000
CELERYD_CONCURRENCY=4
BROKER_URL='amqp://guest:guest@localhost:5672//'
# CELERY_ACCEPT_CONTENT = ['pickle']
# CELERY_TASK_SERIALIZER = ['pickle']
# CELERY_RESULT_SERIALIZER = ['pickle']