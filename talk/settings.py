"""
Django settings for talk project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import django_heroku
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import talk

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nzc$+cynp*a1snm^y=gak_6vpfohqtx(ep#(&d48m6tv445_pd'
CSRF_COOKIE_SECURE=True
# SECURITY WARNING: don't run with debug turned on in production!
import sys
# if len((sys.argv) >=2 and sys.argv[1]=='runserver'):
DEBUG = True
# else:
#     DEBUG = False

ALLOWED_HOSTS = ["*"]

# db = harperdb.HarperDB(
#     url=os.environ["DB_URL"],
#     username=os.environ["DB_USER"],
#     password=os.environ["DB_PASSWORD"])

# Application definition
# CSRF_TRUSTED_ORIGINS = []
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'service',
    'channels',
    'talk',
]



# REDIS_HOSTNAME= os.environ.get( "REDIS_HOSTNAME ")

CSRF_TRUSTED_ORIGINS = ['https://krishna00.herokuapp.com/','http://krishna00.herokuapp.com','https://krishna00.herokuapp.com','https://*.127.0.0.1']

# CACHES = {
#     "default": {
#          "BACKEND": "redis_cache.RedisCache",
#          "LOCATION": os.environ.get('REDIS_URL'),
#          "OPTIONS": {
#             "CONNECTION_POOL_KWARGS": {
#                 "ssl_cert_reqs": False
#             }
#         }
#     }
# }


# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels.layers.InMemoryChannelLayer"
#     }
# }



MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# REDIS_PORT = os.environ.get( "REDIS_PORT" )
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("https://krishna00.herokuapp.com/", 'redis://localhost:6379')],
#         },
#     },
# }

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis://:tCcC4P5rJNBpqyRYwgJEItk4WlgLeJcP@redis-19818.c270.us-east-1-3.ec2.cloud.redislabs.com:19818","'redis://localhost:6379'")],
        },
    },
}


ROOT_URLCONF = 'talk.urls'
CORS_ORIGIN_ALLOW_ALL = True
GOOGLE_RECAPTCHA_SECRET_KEY ="6LekCpUeAAAAANWvmMWtnsur8MbOAVyYA7W5V2S6"
GOOGLE_RECAPTCHA_SITE_KEY ="6LekCpUeAAAAAI2Juw52vAmgVlv9mDP6UMAx659C"
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ASGI_APPLICATION = 'talk.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
WSGI_APLICATION="talk.wsgi.application"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATICFILES_DIRS=[BASE_DIR,'static']


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# django_heroku.settings(locals())

STATIC_URL = '/static/'
STATIC_ROOT= BASE_DIR / 'static'

# SESSION_cOOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# SECURE_HSTS_SECONDS = 31536000 
# SECURE_HSTS_PRELOAD = True
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
