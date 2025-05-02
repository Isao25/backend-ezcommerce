from django.contrib import admin
from .models import *

# Cambiar de ubicación el model Group en el admin Django
from django.contrib.auth.models import Group
Group._meta.app_label = 'epica1'
Group._meta.verbose_name = "Rol"
Group._meta.verbose_name_plural = "Roles"

class UsuarioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Usuario._meta.fields]
    ordering = ('username',)

class GroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Group._meta.fields]
    ordering = ('name',)


admin.site.register(Usuario, UsuarioAdmin)
#admin.site.register(Group, GroupAdmin)