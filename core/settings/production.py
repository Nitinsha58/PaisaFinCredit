from os import environ
from core.settings.shared import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ.get("DJANGO_SECRET_KEY", None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(environ.get("DJANGO_DEBUG", 0)))

ALLOWED_HOSTS = environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
CSRF_TRUSTED_ORIGINS = environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").split(",")


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": environ.get("DJANGO_DATABASE_NAME", None),
        "USER": environ.get("DJANGO_DATABASE_USER", None),
        "PASSWORD": environ.get("DJANGO_DATABASE_PASSWORD", None),
        "HOST": environ.get("DJANGO_DATABASE_HOST", None),
        "PORT": environ.get("DJANGO_DATABASE_PORT", None),
    }
}

INSTALLED_APPS += [
    "storages",
]

# Amazon s3 settings
AWS_S3_ACCESS_KEY_ID = environ.get("AWS_S3_ACCESS_KEY_ID", None)
AWS_S3_SECRET_ACCESS_KEY = environ.get("AWS_S3_SECRET_ACCESS_KEY", None)
AWS_STORAGE_BUCKET_NAME = environ.get("AWS_STORAGE_BUCKET_NAME", None)

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_PRELOAD_METADATA = True

AWS_DEFAULT_ACL = 'public-read'
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400'
}
AWS_HEADERS = { 
    'Access-Control-Allow-Origin': '*',
}

AWS_LOCATION = 'static'
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'