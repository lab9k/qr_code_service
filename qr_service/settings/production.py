from qr_service.settings.base import *

DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.environ.get('SECRET_KEY')
