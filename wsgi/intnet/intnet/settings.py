"""
Django settings for intnet project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import urlparse
from unipath import Path
from sys import path

# a setting to determine whether we are running on OpenShift
ON_OPENSHIFT = True
if 'OPENSHIFT_REPO_DIR' in os.environ:
    ON_OPENSHIFT = True

# if ON_OPENSHIFT:
#     SITE_ROOT = os.environ['OPENSHIFT_APP_NAME'] + "/intnet/"
# else:
SITE_ROOT = Path(__file__).ancestor(2)
INTNET_ROOT = SITE_ROOT.child('dirr_activities')

path.append(INTNET_ROOT)

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'oyu_lkv@pnfd@o_4=)62pk-+165xf6$unb45sbpcce!ggb6350'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'users.DirrUser'

LOGIN_URL = '/login/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'activities',
    'bookings',
    'users',
    'main',
    'crispy_forms'
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'intnet.urls'

WSGI_APPLICATION = 'intnet.wsgi.application'

TEMPLATE_DIRS = (
    SITE_ROOT.child('templates'),
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

if ON_OPENSHIFT:
    url = urlparse.urlparse(os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL'))

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'intnet',
            'USER': url.username,
            'PASSWORD': url.password,
            'HOST': url.hostname,
            'PORT': url.port,
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'intnet',
            'USER': 'developer',
            'PASSWORD': 'developer',
            'HOST': '127.0.0.1',
            'PORT': '5432',
            'OPTIONS': {
                'client_encoding': 'UTF8',
                'autocommit': True,
            },
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    # '/var/lib/openshift/5317194c50044674240000c5/app-root/runtime/repo/static/',
    # ('/var/lib/openshift/5317194c50044674240000c5/python/virtenv/lib/python2.7/site-packages/'
    #  'Django-1.6.2-py2.7.egg/django/contrib/admin/static/'),
)
