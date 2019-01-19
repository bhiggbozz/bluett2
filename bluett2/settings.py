"""
Django settings for bluett2 project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
#import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


import pymysql
pymysql.install_as_MySQLdb()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%dgi_0x98eyc=^atr-fp)8n7cr54t!=$f3u3-_2o+gxksn17zd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'studentapp.apps.StudentappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_mysql',
   # 'crispy_forms',
]

CRISPY_TEMPLATE_PACK = 'boostrap4 '

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
   # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bluett2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

#WSGI_APPLICATION = 'bluett2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
#DATABASES = {
 #     'default': dj_database_url.config(
  #        default='sqlite:////{0}'.format(os.path.join(BASE_DIR, 'db.sqlite3'))
   #   )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',
        'host': '172.31.0.0/16',
        'PASSWORD': 'passworded',
        'USER':'gbiggsDB',
        'NAME': 'users',
        'PORT': '3306',
    },
  # 'main':{
  #  'ENGINE': 'django.db.backends.mysql',
   # 'HOST': 'gbengainstance.cz231tourvfu.eu-central-1.rds.amazonaws.com',
   # 'PASSWORD': 'passworded',
#    'USER':'gbiggsDB',
#    'NAME': 'SINCLAIR',
#    'PORT': '3306',
 #   }

}
#'NAME': get_env_variable('DATABASE_NAME'),
     #   'USER': get_env_variable('DATABASE_USER'),
     #ru   'PASSWORD': get_env_variable('DATABASE_PASSWORD'),
#DATABASES = {
#    'default': {
 #      'ENGINE': 'django.db.backends.sqlite3',
 #       'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
 #   }
#}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#db_from_env = dj_database_url.config(conn_max_age = 500)
#DATABASES = ["default"].update(db_from_env)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATIC_URL = '/static/'
#STATIC_ROOT = ''
STATIC_ROOT =os.path.join(BASE_DIR,'static')
#STATIC_URL =os.path.join(BASE_DIR,'static')

#DATABASE_ROUTERS=['dynamic_db_router.DynamicDbRouter']
#STATIC_URL = os.path.join(BASE_DIR, "/static/")
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#STATICFILES_STORAGE =  "whitenoise.storage.CompressedManifestStaticFilesStorage"