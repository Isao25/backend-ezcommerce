from django.contrib import admin
from .models import *

class OrdenCompraAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrdenCompra._meta.fields]
    ordering = ('id_usuario',)

class DetalleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Detalle._meta.fields]
    ordering = ('id_articulo',)

class TipoMensajeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TipoMensaje._meta.fields]
    ordering = ('nombre',)

class TipoSalaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TipoSala._meta.fields]
    ordering = ('nombre',)

class SalaChatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalaChat._meta.fields]
    ordering = ('id',)

class MensajeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Mensaje._meta.fields]
    ordering = ('id_usuario',)


admin.site.register(OrdenCompra, OrdenCompraAdmin)
admin.site.register(Detalle, DetalleAdmin)
admin.site.register(TipoMensaje, TipoMensajeAdmin)
admin.site.register(TipoSala, TipoSalaAdmin)
admin.site.register(SalaChat, SalaChatAdmin)
admin.site.register(Mensaje, MensajeAdmin)