#importamos AppConfig
from django.apps import AppConfig

# Módulo epica1
class Epica1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'epica1' #nombre del modulo
    verbose_name = "Gestión de Usuarios" #nombre con el que será visible