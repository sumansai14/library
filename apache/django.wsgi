import os
import sys

path = '/home/sai/django/wisecells/library'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'library.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

