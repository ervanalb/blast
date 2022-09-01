"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import os
import sys
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-emj*+kbyrdii%75%z_3@$wizbabb3vgwmyrn)0gsjgtui6ssha"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "host",
    "crispy_forms",
    "django_celery_beat",
    "revproxy",
    "rest_framework",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "host", "templates", "host")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("MYSQL_DATABASE", "blast_db"),
        "USER": os.environ.get("MYSQL_USER", ""),
        "PASSWORD": os.environ.get("MYSQL_ROOT_PASSWORD", "password"),
        "HOST": os.environ.get("DATABASE_HOST", "database"),
        "PORT": os.environ.get("DATABASE_PORT", "3306"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "app/static/")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


MEDIA_URL = "/cutouts/"
# os.path.join(os.path.dirname(BASE_DIR), '../cutout_cdn')

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "../cutout_cdn")
SED_OUTPUT_ROOT = os.path.join(os.path.dirname(BASE_DIR), "../sed_output")
GHOST_OUTPUT_ROOT = os.path.join(os.path.dirname(BASE_DIR), "../ghost_output")
TNS_STAGING_ROOT = os.path.join(os.path.dirname(BASE_DIR), "../tns_staging")
TRANSMISSION_CURVES_ROOT = os.path.join(os.path.dirname(BASE_DIR), "../transmission")

CUTOUT_OVERWRITE = os.environ["CUTOUT_OVERWRITE"]

CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_TIMEZONE = "UTC"

CELERY_IMPORTS = ["host.tasks"]

rabbitmq_user = os.environ.get("RABBITMQ_USERNAME", "guest")
rabbitmq_password = os.environ.get("RABBITMQ_PASSWORD", "guest")
rabbitmq_host = os.environ.get("MESSAGE_BROKER_HOST", "rabbitmq")
rabbitmq_port = os.environ.get("MESSAGE_BROKER_PORT", "5672")

CELERY_BROKER_URL = (
    f"amqp://{rabbitmq_user}:{rabbitmq_password}@{rabbitmq_host}:{rabbitmq_port}//"
)

CELERYD_REDIRECT_STDOUTS_LEVEL = "INFO"
CRISPY_TEMPLATE_PACK = "bootstrap4"

######API########
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        f'rest_framework.permissions.{os.environ.get("API_AUTHENTICATION")}',
    ]
}
