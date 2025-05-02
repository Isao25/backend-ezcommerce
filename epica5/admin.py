from django.contrib import admin
from .models import *

class MarcaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Marca._meta.fields]
    ordering = ('nombre',)

class PlanAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Plan._meta.fields]
    ordering = ('nombre',)

class MembresiaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Membresia._meta.fields]
    ordering = ('id_marca',)

admin.site.register(Marca, MarcaAdmin)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Membresia, MembresiaAdmin)