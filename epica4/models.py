from django.db import models
from epica1.models import *
from epica5.models import Marca
from django.core.exceptions import ValidationError

class Etiqueta(models.Model):
    nombre = models.CharField("Nombre", max_length=50, unique=True)
    descripcion = models.TextField("Descripción")
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"
        db_table = "Etiqueta"


class Catalogo(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name = "Dueño")
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca", null = True, blank = True)
    capacidad_maxima = models.IntegerField("Límite", default=15)
    espacio_ocupado = models.IntegerField("Espacio ocupado", default=0)

    def clean(self):
        super().clean()
        if self.espacio_ocupado > self.capacidad_maxima:
            raise ValidationError("Parece que te quedaste sin espacio. ¡Es un buen momento para actualizar tu plan!")
        
        if self.espacio_ocupado < 0:
            self.espacio_ocupado = 0


    def save(self, *args, **kwargs):
        self.full_clean()  
        if self.espacio_ocupado > 0: 
            self.id_usuario.es_vendedor = True    
            self.id_usuario.save() 
        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        if self.id_marca == None:                    
            self.id_usuario.es_vendedor = False    
            self.id_usuario.save() 
        super().delete(*args, **kwargs)


    def __str__(self):
        if self.id_marca == None:
            return 'Catálogo de ' + self.id_usuario.nombres + ' ' + self.id_usuario.apellido_p + ' ' + self.id_usuario.apellido_m
        else: 
            return 'Catálogo de ' + self.id_marca.nombre
    
    class Meta:
        verbose_name = "Catálogo"
        verbose_name_plural = "Catálogos"
        db_table = "Catalogo"



class Articulo(models.Model):
    id_catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, verbose_name = "Vendedor")
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField("Nombre", max_length=100, unique=True)
    descripcion = models.TextField("Descripción")
    precio = models.FloatField("Precio")
    stock = models.IntegerField("Stock disponible", default=1)
    etiquetas = models.ManyToManyField(Etiqueta)
    disponible = models.BooleanField("Disponible", default=True)
    bloqueado = models.BooleanField("Bloqueado", default=False)

    def save(self, *args, **kwargs):
        # Incrementar el espacio ocupado solo al crear un nuevo artículo.
        if not self.pk:  # Verifica si es un objeto nuevo
            if self.id_catalogo.espacio_ocupado >= self.id_catalogo.capacidad_maxima:
                raise ValidationError("El catálogo ha alcanzado su límite máximo de artículos.")                
            self.id_catalogo.espacio_ocupado += 1
            self.id_catalogo.save()

        if self.stock < 0:
            self.stock = 0
        
        self.disponible = self.stock > 0
        
        if self.precio < 0:
            self.precio = 0

        if self.id_catalogo.id_marca is not None:
            self.id_marca = self.id_catalogo.id_marca
        else:
            self.id_marca = None
        
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Reducir el espacio ocupado al eliminar un artículo.
        if self.id_catalogo.espacio_ocupado > 0:
            self.id_catalogo.espacio_ocupado -= 1
            self.id_catalogo.save()

        super().delete(*args, **kwargs)


    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        db_table = "Articulo"


class Imagen(models.Model):
    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name = "Artículo")
    url = models.URLField("URL")

    def __str__(self):
        return self.id_articulo.nombre
    class Meta:
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"
        db_table = "Imagen"



