from django.contrib import admin
from .models import Facultad, EscuelaProfesional
#Clase Facultad
class FacultadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Facultad._meta.fields]
    ordering = ('nombre',)
#Clase EscuelaProfesional
class EscuelaProfesionalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EscuelaProfesional._meta.fields]
    ordering = ('nombre',)
#Registrar clases en el admin
admin.site.register(Facultad, FacultadAdmin)
admin.site.register(EscuelaProfesional, EscuelaProfesionalAdmin)