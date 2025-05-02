from django.db import models
from epica1.models import Usuario
from epica4.models import Articulo
from django.core.exceptions import ValidationError
from django.views.generic.edit import CreateView

#Gestión de pedidos:

class OrdenCompra(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Comprador")
    fecha_compra = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_usuario.__str__() + ' - ' + str(self.fecha_compra)

    class Meta:
        verbose_name = "Orden de compra"
        verbose_name_plural = "Órdenes de compra"
        db_table = "OrdenCompra"


class Detalle(models.Model): #Detalle del producto
    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name="Articulo")
    id_orden = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE, verbose_name="Orden de Compra #")
    cantidad = models.IntegerField("Cantidad", default=1)

    def clean(self):
        if self.id_articulo.stock == 0:
            self.cantidad = 0
        else:
            if self.cantidad < 1:
                self.cantidad = 1
            elif self.cantidad > self.id_articulo.stock:
                self.cantidad = self.id_articulo.stock

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Detalle de Artículo {self.id_articulo} en Orden {self.id_orden} - Cantidad: {self.cantidad}"
    
    class Meta:
        verbose_name = "Detalle de Artículo"
        verbose_name_plural = "Detalles de Artículos"
        db_table = "Detalle"


#Gestión de Mensajes:

class TipoMensaje(models.Model):
    nombre = models.CharField("Nombre", max_length=30, unique=True)
    descripcion = models.CharField("Descripcion", max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Tipo de Mensaje"
        verbose_name_plural = "Tipos de Mensaje"
        db_table = "TipoMensaje"


class TipoSala(models.Model):
    nombre = models.CharField("Nombre", max_length=30, unique=True)
    descripcion = models.CharField("Descripcion", max_length=100)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Tipo de Sala"
        verbose_name_plural = "Tipos de Sala"
        db_table = "TipoSala"


class SalaChat(models.Model):
    nombre = models.CharField("Nombre", max_length=30, blank = True, null=True)
    tipo = models.ForeignKey(TipoSala, on_delete=models.CASCADE, verbose_name="Tipo de Sala")
    usuarios = models.ManyToManyField(Usuario, related_name="salas", verbose_name="Usuarios en la sala")
       

    def __str__(self):
        return str(self.id) + ' - ' + self.tipo.nombre
    
    class Meta:
        verbose_name = "Sala de Chat"
        verbose_name_plural = "Salas de Chat"
        db_table = "SalaChat"


class Mensaje(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Emisor")
    tipo = models.ForeignKey(TipoMensaje, on_delete=models.CASCADE, verbose_name="Tipo de Mensaje")
    id_sala = models.ForeignKey(SalaChat, on_delete=models.CASCADE, verbose_name="Sala")
    mensaje = models.TextField("Mensaje", max_length=2000)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    url = models.URLField("URL", blank=True, null=True)

    def __str__(self):
        return self.id_usuario.__str__() + ' - ' + str(self.fecha_envio)
    
    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"
        db_table = "Mensaje"


class MensajeCreateView(CreateView):
    model = Mensaje
    fields = ['tipo', 'id_sala', 'mensaje', 'url']  

    def form_valid(self, form):
        form.instance.id_usuario = self.request.user 
        return super().form_valid(form)

