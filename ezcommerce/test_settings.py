from .settings import *

# Base de datos en memoria para tests
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django_filters',
    'corsheaders',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'epica1',
    'epica2',
    'epica4',
    'epica5',
    'epica6',
    'epica8',
    'ezcommerce',
    'rest_framework_simplejwt',
    'drf_yasg'
]

# Desactivar migraciones para tests más rápidos
class DisableMigrations:
    def __contains__(self, item):
        return True
    
    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

# Configuración específica para tests
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]

# Desactivar logging durante tests
LOGGING_CONFIG = None

# Cache dummy para tests
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Configuración de email para tests
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Archivos estáticos para tests
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'