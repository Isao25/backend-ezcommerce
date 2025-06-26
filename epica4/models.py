from django.db import models
from epica1.models import Usuario
from epica5.models import Marca
from django.core.exceptions import ValidationError

#Clase Etiqueta
class Etiqueta(models.Model):
    nombre = models.CharField("Nombre", max_length=50, unique=True)
    descripcion = models.TextField("Descripción")
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Etiqueta" #Nombre con el que será visible
        verbose_name_plural = "Etiquetas" #Nombre con el que será visible el plural
        db_table = "Etiqueta" #Tabla de la bd

#Clase Catalogo
class Catalogo(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name = "Dueño")  #Obligatorio
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name="Marca", null = True, blank = True) 
    capacidad_maxima = models.IntegerField("Límite", default=15)  #Obligatorio
    espacio_ocupado = models.IntegerField("Espacio ocupado", default=0) #automático

    def clean(self):
        super().clean()
        if self.espacio_ocupado > self.capacidad_maxima:
            raise ValidationError("Parece que te quedaste sin espacio. ¡Es un buen momento para actualizar tu plan!")
        #consistencia que evita que el espacio ocupado sea negativo
        if self.espacio_ocupado < 0: 
            self.espacio_ocupado = 0

    def save(self, *args, **kwargs): #método de guardado
        self.full_clean()  
        if self.espacio_ocupado > 0: 
            self.id_usuario.es_vendedor = True    
            self.id_usuario.save() 
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs): #Método de eliminado
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
        verbose_name = "Catálogo" #Nombre con el que será visible
        verbose_name_plural = "Catálogos" #Nombre con el que será visible el plural
        db_table = "Catalogo" #Tabla de la bd

#Clase Articulo
class Articulo(models.Model):
    id_catalogo = models.ForeignKey(Catalogo, on_delete=models.CASCADE, verbose_name = "Vendedor") #Obligatorio
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField("Nombre", max_length=100, unique=True) #Obligatorio
    descripcion = models.TextField("Descripción") #Obligatorio
    precio = models.FloatField("Precio") #Obligatorio
    stock = models.IntegerField("Stock disponible", default=1) #Obligatorio / automático
    etiquetas = models.ManyToManyField(Etiqueta) #Obligatorio
    disponible = models.BooleanField("Disponible", default=True) #automático
    bloqueado = models.BooleanField("Bloqueado", default=False) #automático

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
        verbose_name = "Articulo" #Nombre con el que será visible
        verbose_name_plural = "Articulos" #Nombre con el que será visible el plural
        db_table = "Articulo" #Tabla de la bd

#Clase Imagen
class Imagen(models.Model):
    id_articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, verbose_name = "Artículo") #Obligatorio
    url = models.URLField("URL") #Obligatorio 

    def __str__(self):
        return self.id_articulo.nombre
    class Meta:
        verbose_name = "Imagen" #Nombre con el que será visible
        verbose_name_plural = "Imagenes" #Nombre con el que será visible el plural
        db_table = "Imagen" #Tabla de la bd



