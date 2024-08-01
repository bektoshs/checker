from pathlib import Path
import os
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yq71ac#o2-$vwt-#60h(z&q_h241zid2_6aww!$^jnon+*ucx^'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = True


ALLOWED_HOSTS = ['*']
#ALLOWED_HOSTS = ['trust-api.asakabank.uz', '172.16.53.77', '127.0.0.1', 'localhost', '192.168.84.47']



CSRF_TRUSTED_ORIGINS = [
    'https://trust-api.asakabank.uz',
    'https://172.16.53.77:8080',
    'https://89.249.63.66:8080',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'import_export',
    'checker',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'checker.middleware.AdminAccessControlMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

#CORS_ALLOWED_ORIGINS = [
#   'https://trust.asakabank.uz',
#   'https://trust-api.asakabank.uz'
#]

CORS_ALLOW_HEADERS = ['content_type', 'x-csrftoken', 'authorization', 'x-requested-with']

#CSRF_TRUSTED_ORIGINS = [
#    'https://trust-api.asakabank.uz',
#
#    'https://trust.asakabank.uz'
#]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

ROOT_URLCONF = 'website_status.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'website_status.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# Prod
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql',
         'NAME': os.getenv('POSTGRES_DB'),
         'USER': os.getenv('POSTGRES_USER'),
         'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
         'HOST': os.getenv('POSTGRES_HOST', 'db'),
         'PORT': os.getenv('POSTGRES_PORT', '5432'),
     }
}

# Local
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'databse_real',
#        'USER': 'postgres',
#        'PASSWORD': '0525',
#        'HOST': 'db',
#        'PORT': '5432',
#    }
#}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


IMPORT_EXPORT_USE_TRANSACTIONS = True
IMPORT_EXPORT_SKIP_ADMIN_LOG = False
IMPORT_EXPORT_IMPORT_PERMISSION_CODE = 'import_data'
IMPORT_EXPORT_EXPORT_PERMISSION_CODE = 'export_data'



if os.getenv("ENABLE_OTEL", "False") == "True":
    from opentelemetry import trace
    from opentelemetry.sdk.resources import Resource
    from opentelemetry.sdk.trace import TracerProvider
    from opentelemetry.sdk.trace.export import BatchSpanProcessor
    from opentelemetry.exporter.jaeger.thrift import JaegerExporter

    # Checking site get or create service
    check_website_resource = Resource(attributes={
        "service.name": "check_website_service"
    })

    check_website_provider = TracerProvider(resource=check_website_resource)
    trace.set_tracer_provider(check_website_provider)
    check_website_tracer = trace.get_tracer("check_website_tracer")

    check_website_exporter = JaegerExporter(
        agent_host_name='localhost',
        agent_port=6831,
    )

    check_website_span_processor = BatchSpanProcessor(check_website_exporter)
    check_website_provider.add_span_processor(check_website_span_processor)

    # List website service
    list_website_resource = Resource(attributes={
        "service.name": "list_website_service"
    })

    list_website_provider = TracerProvider(resource=list_website_resource)
    trace.set_tracer_provider(list_website_provider)
    list_website_tracer = trace.get_tracer("list_website_tracer")

    list_website_exporter = JaegerExporter(
        agent_host_name='localhost',
        agent_port=6831,
    )

    list_website_span_processor = BatchSpanProcessor(list_website_exporter)
    list_website_provider.add_span_processor(list_website_span_processor)
else:
    check_website_tracer = None
    list_website_tracer = None
