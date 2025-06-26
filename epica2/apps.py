from django.apps import AppConfig #importamos AppConfig
# Módulo epica2
class Epica2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'epica2' #nombre del modulo
    verbose_name = "Datos Académicos" #nombre con el que será visible