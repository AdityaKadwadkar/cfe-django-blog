"""
Django settings for cfeblog project.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

if ENV_PATH.exists():
    load_dotenv(str(ENV_PATH))

# === SECURITY ===
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "render_dummy_secret_key")

DEBUG = str(os.environ.get("DJANGO_DEBUG", "0")) == "1"

# Render sets the hostname automatically
ALLOWED_HOSTS = ["*",]

# === APPS ===
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "articles",
]

# === MIDDLEWARE ===
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",

    # Whitenoise for static files in Render
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# === URL / WSGI ===
ROOT_URLCONF = "cfeblog.urls"
WSGI_APPLICATION = "cfeblog.wsgi.application"

# === TEMPLATES ===
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# === DATABASE (SQLite for Render free tier) ===
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# DO NOT use MySQL or Postgres unless explicitly set
DATABASE_BACKEND = os.environ.get("DATABASE_BACKEND")
if DATABASE_BACKEND == "mysql":
    from .dbs.mysql import *  # noqa
elif DATABASE_BACKEND == "postgres":
    from .dbs.postgres import *  # noqa

# === PASSWORDS ===
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# === INTERNATIONALIZATION ===
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# === STATIC / MEDIA ===
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticroot"

# Remove STATICFILES_DIRS because project does not use it
# STATICFILES_DIRS = [BASE_DIR / "staticfiles"]

# Whitenoise compression
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "mediafiles"

# === STORAGE CONFIG ===
# This project has optional cloud storage modules.
# They will be ignored unless you configure django-storages.
from .storages.conf import *  # noqa

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
