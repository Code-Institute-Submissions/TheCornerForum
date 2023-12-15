"""
WSGI config for earnsforum project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise
from django.core.wsgi import get_wsgi_application


from earnsforum import users1
from earnsforum import blog

users1 = WhiteNoise(users1, root='users1/static')
blog = WhiteNoise(blog, root='blog/static')



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'earnsforum.settings')

application = get_wsgi_application()
