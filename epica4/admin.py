from django.contrib import admin
from .models import Etiqueta, Catalogo, Articulo, Imagen
#Clase Etiqueta
class EtiquetaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Etiqueta._meta.fields]
    ordering = ('nombre',)
#Clase Catalogo
class CatalogoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Catalogo._meta.fields]
    ordering = ('id_usuario',)
#Clase Articulo
class ArticuloAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Articulo._meta.fields]
    ordering = ('nombre',)
#Clase Imagen
class ImagenAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Imagen._meta.fields]
    ordering = ('id_articulo',)
#Registrar clases en el admin
admin.site.register(Etiqueta, EtiquetaAdmin)
admin.site.register(Catalogo, CatalogoAdmin)
admin.site.register(Articulo, ArticuloAdmin)
admin.site.register(Imagen, ImagenAdmin)