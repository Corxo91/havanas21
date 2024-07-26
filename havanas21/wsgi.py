import os
import sys
path = os.path.expanduser('~/havanas21')
if path not in sys.path:
    sys.path.insert(0,path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'havanas21.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
<<<<<<< HEAD
application = StaticFilesHandler(get_wsgi_application())
=======
application = StaticFilesHandler(get_wsgi_application())
>>>>>>> 800db762a542d7ba1511d3ceaf6b32a37e3cc2ec
