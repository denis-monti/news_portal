"""
Django settings for news_main project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path


import corsheaders.middleware
import django.core.mail.backends.console
import django_redis.cache
from django.contrib import messages
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MESSAGE_LEVEL = messages.DEBUG

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sa(hzy0che=6^9tscmwam1vba=spc8*oq6!e%u_e@itln(z9_&'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False
#
# ALLOWED_HOSTS = ['www.supersite.ru', '127.0.0.1']

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    # my modules or applications #
    'news_output',
    'news_main',
    'news_auth_registered',
    # elastic search#
    # 'django_elasticsearch_dsl',
    #redis#
    # 'django_redis',
    # captcha # 
    'captcha',
    'rest_framework',
    'corsheaders',
    'django_cleanup',
    #форматирование страниц под html разметку#
    'precise_bbcode',
    # для формирование миниатюр#
    'easy_thumbnails',
    # авторизация на сайте через стороние сервисы#
    'social_django',
    #приложение для непонятного #
    'api'
]

# EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'

EMAIL_HOST='smtp.mail.ru'
EMAIL_PORT=587
EMAIL_USE_TLS=1
EMAIL_HOST_USER='*****'
EMAIL_HOST_PASSWORD='*****'
EMAIL_TIMEOUT = 15
SERVER_EMAIL=EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


CORS_ORIGIN_ALLOW_ALL = True
CORS_URL_REGEX = r'^/api/.*$'


ADMIN = [
    ('denchik', 'sinde.blow@gmail.com')
]
#Хранение данных типа json#
SOCIAL_AUTH_JSONFIELD_ENABLED = True

#id приложение полученное ранее #
SOCIAL_AUTH_VK_OATH2_KEY = 'XXXXXXX'

#защищеный ключ полученный ранее#
SOCIAL_AUTH_VK_OATH2_SECRET = 'ХХХХХХХХХХХХХХХХХХХХ'

#от сети, из которой поступил запрос на авторизацию#
SOCIAL_AUTH_VK_OATH2_SCOPE = ['email']

#классы ррееальизующие аутеентификацию#
AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

# для капчи менять знак умножение#
CAPTCHA_MATH_CHALLENGE_OPERATOR = 'x'





# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://localhost:6379/0'
#     },
#     'session_storage': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://localhost:6379'
#     }
# }

# SESSION_ENGINE='django.contrib.sessions.backends.cache'
#
# SESSION_CACHE_ALIAS='session_storage'

# CACHES = {
#     'default': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://localhost:6379/0'
#     },
#     'session_storage': {
#         'BACKEND': 'django_redis.cache.RedisCache',
#         'LOCATION': 'redis://localhost:6379/2'
#     }
# }

# SESSION_ENGINE='django.contrib.sessions.backends.cache'
#
# SESSION_CACHE_ALIAS='session_storage'


THUMBNAIL_ALIASES = {
    '': {
        'default': {
            'size': (200, 0)
        }
    }
}

THUMBNAIL_MEDIA_ROOT = os.path.join(BASE_DIR, 'common_file/media/small_img/')

THUMBNAIL_MEDIA_URL = '/media/small_img'

# ELASTICSEARCH_DSL={
#     'default': {
#         'hosts': 'http://localhost:9200'
#     },
# }

# максимально допустимый объем полученных от
# посетителя данных в виде числа в байтах от dos#
DATA_UPLOAD_МAХ_MEMORY_SIZE = 2621440
#максимально допустимое количество РОSТ-параметров в полученном запросе (т. е. полей в выведенной форме). от  dos#
DATA_UPLOAD_MAX_NUMBER_FIELDS = 1000


MIDDLEWARE = [
    # для rest_framework #
    'corsheaders.middleware.CorsMiddleware',


    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ##
    'corsheaders.middleware.CorsMiddleware',
    ##
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #добавление данных после формирование контекста#
    'news_output.middlewares.RubricsMiddleware',
]

ROOT_URLCONF = 'news_main.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'common_file/templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.csrf',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #для авторизации через социалки#
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                #добавление данных до контекста#
                # 'news_output.middlewares.rubrics'
            ],
        },
    },
]

WSGI_APPLICATION = 'news_main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'news_django',
            'USER': 'postgres',
            'PASSWORD': 'roller0099',
            'HOST': 'localhost',
            'PORT': '',
        }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'common_file/static/'),
)



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = 'news_output:index'


LOGIN_URL = 'news_auth_registered:login'




MEDIA_ROOT = os.path.join(BASE_DIR, 'common_file/media')

MEDIA_URL = 'common_file/media/'

# как модель пользователя, используемая подсистемой разграничения доступа Django
AUTH_USER_MODEL = 'news_auth_registered.AdvUser'

def info_filter(message):
    return message.levelname == 'INFO'

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse',
#         },
#         'require_debug_true': {
#             '()': 'django.utils.log.RequireDebugTrue'
#         },
#     },
#     'formatters': {
#         'simple': {
#             'format': '[%(asctime)s] % (levelname)s: %(message)s',
#             'datefmt': '%Y.%m.%d %H:%M:%S',
#         }
#     },
#     'handlers': {
#         'console_dev': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#             'filters': ['require_debug_true'],
#         },
#         'console_prod': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#         },
#         'file': {
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'c:/news_portal/django-site.log',
#             'maxBytes': 1048576,
#             'backupCount': 10,
#             'formatter': 'simple',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console_dev', 'console_prod'],
#         },
#         'django.server': {
#             'handlers': ['file'],
#             'level': 'INFO',
#             'propagate': True,
#         },
#     }
# }