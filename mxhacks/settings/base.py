import environ

BASE_DIR = environ.Path(__file__) - 3


env = environ.Env()

DJANGO_APPS = (
    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Admin
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'rest_framework',
)

LOCAL_APPS = (
    'contact',
    'hackers',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

DEBUG = env.bool('DJANGO_DEBUG', False)

FIXTURE_DIRS = (str(BASE_DIR.path('fixtures')),)

ADMINS = (
    ('Pablo Trinidad', 'p@ihk.io'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': env.db('DATABASE_URL')
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

TIME_ZONE = 'America/Mexico_City'

LANGUAGE_CODE = 'es-mx'

USE_I18N = True

USE_L10N = True

USE_TZ = False

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(BASE_DIR.path('templates')),
        ],
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

STATIC_ROOT = str(BASE_DIR('staticfiles'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    str(BASE_DIR.path('static')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIA_ROOT = str(BASE_DIR('media'))
MEDIA_URL = '/media/'

ROOT_URLCONF = 'mxhacks.urls'
APPEND_SLASH = True

WSGI_APPLICATION = 'mxhacks.wsgi.application'

ADMIN_URL = 'admin'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

MAILGUN_ENDPOINT = env('MAILGUN_ENDPOINT')
MAILGUN_API_KEY = env('MAILGUN_API_KEY')

SPONSORS_MAIL = env('SPONSORS_MAIL')
SUPPORT_MAIL = env('SUPPORT_MAIL')