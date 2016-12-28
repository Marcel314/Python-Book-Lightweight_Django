"""
Django settings for SiteBuilder project.
"""

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'uw=z!)v1#o@pdxo5agfkr^#a47c*)t(3l@k(u*qwbvy=x0j1r('
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.webdesign',
    'django.contrib.staticfiles',
    'SiteBuilderApp',
    #'compressor',
)
MIDDLEWARE_CLASSES = (
)
ROOT_URLCONF = 'SiteBuilder.urls'
WSGI_APPLICATION = 'SiteBuilder.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files
STATIC_URL = '/static/'
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)
STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), '../static/'),
)
SITE_PAGES_DIR = os.path.join(BASE_DIR,'pages')
SITE_OUTPUT_DIR = os.path.join(BASE_DIR,'_build')
STATIC_ROOT = os.path.join(BASE_DIR,'_build','static')
"""
STATICFILES_FINDERS=(
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        'compressor.finders.CompressorFinder',
    )
"""

#STATICFILES_STORAGE='django.contrib.staticfiles.storage.CachedStaticFilesStorage'