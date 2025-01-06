# settings.py
import os
from pathlib import Path
from datetime import timedelta
from django.conf import settings
from django.conf.urls.static import static



# BASE_DIR es el directorio raíz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY: Cambia esto por una clave secreta única
SECRET_KEY = 'tu_clave_secreta_aqui'

# DEBUG: Asegúrate de establecer esto a False en producción
DEBUG = True

# ALLOWED_HOSTS: Aquí debes agregar los dominios donde tu aplicación estará disponible (vacío para desarrollo)
ALLOWED_HOSTS = []

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'usuarios',  # Asegúrate de que esté incluida
    'rest_framework',  # Para la API RESTful
    'rest_framework.authtoken',
    'rest_framework_simplejwt',  # Para JWT
    'rest_framework_simplejwt.token_blacklist',

]

# Middleware: aquí se define cómo Django maneja las solicitudes
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_HEADERS = [
    'content-type',
    'authorization',
    'x-csrf-token',
]
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # Dirección del frontend
]

# La URL raíz de tu proyecto
ROOT_URLCONF = 'Proyecto_Ropa.urls'

# El directorio de plantillas HTML (no es obligatorio para tu API, pero si usas vistas)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# El WSGI application
WSGI_APPLICATION = 'Proyecto_Ropa.wsgi.application'

# Configuración de la base de datos (en este caso, SQLite, puedes cambiar a PostgreSQL o MySQL si prefieres)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Contraseña de seguridad
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

#
# settings.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}


# Configuración del JWT
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),  # Tiempo de vida del token de acceso
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),  # Tiempo de vida del token de refresco
    'ROTATE_REFRESH_TOKENS': False,  # Si deseas que los tokens de refresco roten
    'BLACKLIST_AFTER_ROTATION': True,  # Si se invalidan los tokens antiguos
    'UPDATE_LAST_LOGIN': False,  # No actualizar el último login automáticamente
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Configuración de la localización
LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Directorio de subida de imágenes
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Archivos estáticos
STATIC_URL = '/static/'

from datetime import timedelta

