"""
WSGI config for Holder project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import  Holder.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Holder.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
print("\nApplication Configuration: ")
print("BASE_DIR : ",Holder.settings.BASE_DIR)
print("STATIC_URL : ",Holder.settings.STATIC_URL)
print("STATIC_FILE_DIRS : ",Holder.settings.STATIC_FILE_DIRS)
print("TEMPLATE_DIRS : ",Holder.settings.TEMPLATE_DIRS)
