"""
WSGI config for SiteBuilder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
from SiteBuilder import settings as conf

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SiteBuilder.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

print('\n# Current configuration:')
print('BASE_DIR: ',conf.BASE_DIR)
print('TEMPLATE_DIRS: ',conf.TEMPLATE_DIRS)
print('STATIC_URL: ',conf.STATIC_URL)
print('ALLOWED_HOSTS: ',conf.ALLOWED_HOSTS)
print('SITE_PAGES_DIR: ',conf.SITE_PAGES_DIR)
print('ROOT_URLCONF: ',conf.ROOT_URLCONF)

print('\n# Info: \nDIRNAME: ',os.path.dirname(__file__))