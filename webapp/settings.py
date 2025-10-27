import os
import sys
from pathlib import Path
import glob

# ==================== RUTAS BASE ====================
BASE_DIR = Path(__file__).resolve().parent.parent

# Agrega el directorio raíz al sys.path para que Python pueda importar 'modules'
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

# ==================== CONFIGURACIONES GENERALES ====================
SECRET_KEY = 'your-secret-key'
DEBUG = True  # ⚠️ Cambia a False en producción

# ==================== HOSTS PERMITIDOS ====================
# Incluye dominios locales y los de Azure
ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
    "[::1]",
    "dimsor.azurewebsites.net",
    "dimsor-cyhwdmf2c8fec8cm.canadacentral-01.azurewebsites.net",
    ".azurewebsites.net"  # Permite cualquier subdominio de Azure
]

# ==================== APLICACIONES INSTALADAS ====================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "core",
    # Agrega aquí tus apps adicionales si las tienes
    # Ejemplo: 'modules.public.sesiones'
]

# ==================== MIDDLEWARE ====================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # 🔥 para servir archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ==================== CONFIGURACIÓN DE URLS Y WSGI ====================
ROOT_URLCONF = 'webapp.urls'
WSGI_APPLICATION = 'webapp.wsgi.application'

# ==================== TEMPLATES ====================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

# ==================== BASE DE DATOS ====================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dimsor',
        'USER': 'root',
        'PASSWORD': 'dominid',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

# ==================== VALIDADORES DE CONTRASEÑA ====================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ==================== CONFIGURACIÓN REGIONAL ====================
LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Lima'
USE_I18N = True
USE_TZ = True

# ==================== ARCHIVOS ESTÁTICOS ====================
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Agrega todas las carpetas static dentro de modules/*/*/static
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Archivos estáticos globales
]
for static_dir in glob.glob(str(BASE_DIR / "modules" / "*" / "*" / "static")):
    STATICFILES_DIRS.append(static_dir)

# WhiteNoise: sirve archivos estáticos en producción
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# ==================== AUTO FIELD ====================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ==================== DEBUG EXTRA OPCIONAL ====================
# (Usa esto temporalmente para saber qué dominio llega al servidor)
# Puedes descomentar para probar:
"""
import socket
print("🌐 Servidor iniciado en host:", socket.gethostname())
"""
