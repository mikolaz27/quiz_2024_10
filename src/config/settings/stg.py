from config.settings.base import *  # NOQA

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-ql(&pwl22zi1_#qb!+huknes8_sd9-7jbd&=(=9y2qgfpm97#0"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
