from qr_service.settings.base import *

DEBUG = bool(os.environ.get('DEBUG', False))

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY')
