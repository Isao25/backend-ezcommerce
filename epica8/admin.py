from django.contrib import admin
from .models import *

class ReporteAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reporte._meta.fields]
    ordering = ('titulo',)

admin.site.register(Reporte, ReporteAdmin)