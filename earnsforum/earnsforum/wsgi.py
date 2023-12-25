import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'earnsforum.settings')

# Get the WSGI application object for the Django project
application = get_wsgi_application()

# Wrap the entire Django application with WhiteNoise
application = WhiteNoise(application)
