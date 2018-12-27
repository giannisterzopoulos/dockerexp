import os
from decouple import Config, RepositoryEnv
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
# BASE_DIR = here('..', '..')
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DOTENV_FILE = os.path.join(here('..', '..'), 'config/postgres/myproject.env')
print('-----------')
print(DOTENV_FILE)

env_config = Config(RepositoryEnv(DOTENV_FILE))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    'django_extensions',
    'rest_framework',
    'corsheaders',

    'myproject.front',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'corsheaders.middleware.CorsMiddleware',    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

# Specify authorized hostnames in CORS_ORIGIN_WHITELIST
CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'myproject/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '5/sec',
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}

WSGI_APPLICATION = 'myproject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': env_config.get('POSTGRES_USER'),
        'NAME': env_config.get('POSTGRES_DB'),
        'PASSWORD': env_config.get('POSTGRES_PASSWORD'),
        'HOST': env_config.get('POSTGRES_SERVICE'),
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'  # Default language that Django will use if no translation is found

LOCALE_PATHS = (
    os.path.join(os.path.abspath(BASE_DIR), 'locale'),
)

TIME_ZONE = 'Europe/Athens'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Login urls
LOGIN_URL = '/login/'

# Static files
__base = BASE_DIR

# print(BASE_DIR)
# print()

# print(__base)

# if os.path.basename(os.path.abspath(BASE_DIR)) == 'src':
#     __base = os.path.abspath(os.path.join(BASE_DIR, os.pardir))

# print(__base)

# __base = '/opt/djangoapp/src'

# tmp_base = os.path.dirname(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
# STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), '..', 'static')

print('---------')
# print(DOTENV_FILE)
print(STATIC_ROOT)

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(__base, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(__base, 'media')
