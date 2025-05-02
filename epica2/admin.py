from django.contrib import admin
from .models import *

class FacultadAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Facultad._meta.fields]
    ordering = ('nombre',)

class EscuelaProfesionalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EscuelaProfesional._meta.fields]
    ordering = ('nombre',)

admin.site.register(Facultad, FacultadAdmin)
admin.site.register(EscuelaProfesional, EscuelaProfesionalAdmin)