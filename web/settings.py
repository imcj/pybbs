import os, sys
ROOT = os.path.join ( os.path.dirname ( __file__ ), ".." ) 
WEB_ROOT = os.path.dirname ( __file__ )
DEBUG = True
TEMPLATE_DEBUG = DEBUG
sys.path.insert(0, ROOT)
sys.path.insert(0, WEB_ROOT)
sys.path.insert(0, os.path.join(ROOT, "lib"))
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'dev.sqlite3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Aisa/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-CN'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join ( WEB_ROOT, "media" )
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+-!d%$mcl4xwbzv0dna4!e%igcdnh1gzvf!lfx5rry&7qg%jcj'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'web.urls'

TEMPLATE_DIRS = (
    os.path.join ( WEB_ROOT, "templates" ),
)


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'south',
    'pybbs',
    'userprofile',
    'siteprofile',
    'django_hudson',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "userprofile.context_processors.site",
    "userprofile.context_processors.css_classes",
)

PROJECT_APPS = (
    'pybbs',
)

AUTH_PROFILE_MODULE = 'siteprofile.profile'
I18N_URLS = False
DEFAULT_AVATAR = os.path.join ( MEDIA_ROOT, 'userprofile/generic.bmp')
AVATAR_WEBSEARCH = False
# 127.0.0.1:8000 Google Maps API Key
#GOOGLE_MAPS_API_KEY = "ABQIAAAA06IJoYHDPFMx4u3hTtaghxTpH3CbXHjuCVmaTc5MkkU4wO1RRhST5bKY_U7dUG1ZGu1S-n-ukXGNjQ"
# Haddock
#GOOGLE_MAPS_API_KEY="ABQIAAAA06IJoYHDPFMx4u3hTtaghxS1mGAeXhF8eEwoOC3WUqD9xSVHbhT_wvgbriWemZzoPwFT5-HqnLJ9-A"
REQUIRE_EMAIL_CONFIRMATION = False
AVATAR_QUOTA = 8