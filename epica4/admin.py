from django.contrib import admin
from .models import *

class EtiquetaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Etiqueta._meta.fields]
    ordering = ('nombre',)

class CatalogoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Catalogo._meta.fields]
    ordering = ('id_usuario',)

class ArticuloAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Articulo._meta.fields]
    ordering = ('nombre',)

class ImagenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Imagen._meta.fields]
    ordering = ('id_articulo',)

admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Catalogo, CatalogoAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Imagen, ImagenAdmin)