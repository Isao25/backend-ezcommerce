from django.contrib import admin
from .models import Usuario
from django.contrib.auth.models import Group

Group._meta.app_label = 'epica1' #módulo
Group._meta.verbose_name = "Rol"
Group._meta.verbose_name_plural = "Roles"

#Clase Usuario
class UsuarioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Usuario._meta.fields]
    ordering = ('username',)

#Clase Grupo
class GroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Group._meta.fields]
    ordering = ('name',)

#Registrar clases en el admin
admin.site.register(Usuario, UsuarioAdmin)
