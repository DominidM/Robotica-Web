import os
import sys
from pathlib import Path
import glob

BASE_DIR = Path(__file__).resolve().parent.parent

# Agrega el directorio raíz al sys.path para que Python pueda importar 'modules'
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

SECRET_KEY = 'your-secret-key'
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "[::1]"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "core",
    # Puedes agregar aquí apps tradicionales si tienes
    # Ejemplo: 'modules.public.sesiones', si la defines como app Django
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

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Si tienes una carpeta global de templates en la raíz del proyecto (Robotica-Web/templates/)
            # Pon aquí: BASE_DIR / "templates"
            # Si NO tienes, déjalo como []
        ],
        'APP_DIRS': True,  # ¡Esto es lo que permite que Django busque en core/templates/!
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

WSGI_APPLICATION = 'webapp.wsgi.application'

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

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'

# Automatiza la búsqueda de todas las carpetas static en modules/*/*/static
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Para archivos estáticos globales si tienes
]
for static_dir in glob.glob(str(BASE_DIR / "modules" / "*" / "*" / "static")):
    STATICFILES_DIRS.append(static_dir)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'