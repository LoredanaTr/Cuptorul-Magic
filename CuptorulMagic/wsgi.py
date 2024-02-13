"""
WSGI config for CuptorulMagic project.

It exposes the WSGI cdeactivateallable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CuptorulMagic.settings')

application = get_wsgi_application()
