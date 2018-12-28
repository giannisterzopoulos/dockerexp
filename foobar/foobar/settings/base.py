import os
from decouple import Config, RepositoryEnv
from django.utils.translation import ugettext_lazy as _


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
here = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)
BASE_DIR = here('..', '..')

DOTENV_FILE = os.path.join(BASE_DIR, '..', 'config/postgres/foobar.env')
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

    # 'foobar.',
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

ROOT_URLCONF = 'foobar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'foobar/templates'),
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

WSGI_APPLICATION = 'foobar.wsgi.application'

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
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = '../static/'
MEDIA_ROOT = '../media/'
