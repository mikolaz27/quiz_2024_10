import os

from config.settings.base import *  # NOQA

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost']


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# /var/www/quiz/static

STATIC_ROOT = BASE_DIR / 'static/'  # NOQA
STATIC_URL = "static/"

MEDIA_ROOT = BASE_DIR / 'media/'  # NOQA
MEDIA_URL = "media/"

