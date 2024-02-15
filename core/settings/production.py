import json
from core.settings.shared import *

# Read configuration from the JSON file
with open('/etc/config.json') as f:
    config = json.load(f)

# Django settings
SECRET_KEY = config.get("DJANGO_SECRET_KEY", None)
DEBUG = bool(int(config.get("DJANGO_DEBUG", 0)))
ALLOWED_HOSTS = config.get("DJANGO_ALLOWED_HOSTS", [])
CSRF_TRUSTED_ORIGINS = config.get("DJANGO_CSRF_TRUSTED_ORIGINS", [])

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# Database settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config.get("DJANGO_DATABASE_NAME", None),
        "USER": config.get("DJANGO_DATABASE_USER", None),
        "PASSWORD": config.get("DJANGO_DATABASE_PASSWORD", None),
        "HOST": config.get("DJANGO_DATABASE_HOST", None),
        "PORT": config.get("DJANGO_DATABASE_PORT", None),
    }
}

# AWS S3 settings
AWS_S3_ACCESS_KEY_ID = config.get("AWS_S3_ACCESS_KEY_ID", None)
AWS_S3_SECRET_ACCESS_KEY = config.get("AWS_S3_SECRET_ACCESS_KEY", None)
AWS_STORAGE_BUCKET_NAME = config.get("AWS_STORAGE_BUCKET_NAME", None)

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