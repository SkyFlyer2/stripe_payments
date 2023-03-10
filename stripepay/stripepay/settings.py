"""
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = str(os.getenv('SECRET_KEY', default='*'))
STRIPE_PUBLISHABLE_KEY = str(os.getenv('STRIPE_PUBLISHABLE_KEY', default='*'))
STRIPE_SECRET_KEY = str(os.getenv('STRIPE_SECRET_KEY', default='*'))

DEBUG = False

ALLOWED_HOSTS = ['*']

if not DEBUG:
    DOMAIN_URL = 'http://158.160.4.20/'
if DEBUG:
    DOMAIN_URL = 'http://127.0.0.1:8000/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'djmoney',
    'payments',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'stripepay.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'stripepay.wsgi.application'
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
CSRF_TRUSTED_ORIGINS = ['http://158.160.4.20']

LANGUAGE_CODE = 'ru-RU'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

AUTH_USER_MODEL = 'users.User'

STATIC_URL = 'static/'
if not DEBUG:
    STATIC_ROOT = str(BASE_DIR / 'static/')
if DEBUG:
    STATICFILES_DIRS = [str(BASE_DIR / 'static')]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
