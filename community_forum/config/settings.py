"""
Django settings for config_forum project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from os.path import join

from configurations import Configuration, values

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

class Common(Configuration):

    SECRET_KEY = '^6%*7r#9bw@5s&h+ixe23b)b@qiohv#zyr1o=ges!@)gp%cuwp'
    
    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(False)
    
    TEMPLATE_DEBUG = DEBUG
    
    ALLOWED_HOSTS = []
    
    
    # Application definition
    
    DJANGO_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    )

    THIRD_PARTY_APPS = (
        'south', # Database migration helpers
        'crispy_forms', # Form layouts
        'avatar', # for user avatars
        'django_extensions',
    )

    LOCAL_APPS = (
        'forum',
        'users',
        'core',
    )

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

    INSTALLED_APPS += (
        # Need to come last for now because of a weird edge case between
        # South and allauth
        'allauth', # registration
        'allauth.account', #registration
        'allauth.socialaccount', #registration
    )    
    
    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )
    
    ROOT_URLCONF = 'config.urls'
    
    WSGI_APPLICATION = 'config.wsgi.application'
    
    
    # Database
    # https://docs.djangoproject.com/en/1.6/ref/settings/#databases
    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    
    # Internationalization
    # https://docs.djangoproject.com/en/1.6/topics/i18n/
    
    LANGUAGE_CODE = 'en-us'

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
    SITE_ID = 1
    
    TIME_ZONE = 'UTC'
    
    USE_I18N = True
    
    USE_L10N = True
    
    USE_TZ = True
    
    
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.6/howto/static-files/
    
    STATIC_URL = '/static/'

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        "allauth.account.context_processors.account",
        "allauth.socialaccount.context_processors.socialaccount",
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request',
        # Your stuff: custom template context processers go here
    )

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    TEMPLATE_DIRS = (
        join(BASE_DIR, 'templates'),
    )

    TEMPLATE_LOADERS = (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )

    # See: http://django-crispy-forms.readthedocs.org/en/latest/install.html#template-packs
    CRISPY_TEMPLATE_PACK = 'bootstrap3'
    ########## END TEMPLATE CONFIGURATION

    STATIC_ROOT = join(os.path.dirname(BASE_DIR), 'venuemonk/staticfiles/')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
    STATIC_URL = '/static/'

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
    STATICFILES_DIRS = (
        ('assets', join(BASE_DIR, 'static')),
    )

    # See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )
    ########## END STATIC FILE CONFIGURATION

    ########## MEDIA CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
    MEDIA_ROOT = join(BASE_DIR, 'media')

    # See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
    MEDIA_URL = '/media/'
    ########## END MEDIA CONFIGURATION

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    # Some really nice defaults
    ACCOUNT_AUTHENTICATION_METHOD = "username"
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"
    ########## END AUTHENTICATION CONFIGURATION

    LOGIN_REDIRECT_URL = "users:redirect"

class Local(Common):

    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG
    
    INSTALLED_APPS = Common.INSTALLED_APPS

    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)

    INSTALLED_APPS += ('debug_toolbar',)

    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    ########## end django-debug-toolbar

    ########## Your local stuff: Below this line define 3rd party libary settings
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    DEFAULT_FROM_EMAIL = values.Value('namaste@venuemonk.com')
    EMAIL_HOST = values.Value('smtp.live.com')
    EMAIL_HOST_PASSWORD = 'rahul@pallav'
    EMAIL_HOST_USER = 'namaste@venuemonk.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
