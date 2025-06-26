from django.db import models
#Clase Facultad
class Facultad(models.Model):
    codigo = models.CharField("Código", max_length = 10, unique = True)
    nombre = models.CharField("Nombre", max_length = 100)
    siglas = models.CharField("Siglas", max_length = 20)
    def __str__(self):
        return self.nombre + ' ('+ self.siglas +')'
    #Clase Meta
    class Meta:
        verbose_name = "Facultad" #nombre con el que será visible
        verbose_name_plural = "Facultades"#nombre con el que será visible el plural
        db_table = "Facultad" #Tabla asociada

#Clase EscuelaProfesional
class EscuelaProfesional(models.Model):
    id_facultad = models.ForeignKey(Facultad, on_delete = models.CASCADE, verbose_name = "Facultad") #FK referencia a Facultad
    codigo = models.CharField("Código", max_length = 10, unique = True)
    nombre = models.CharField("Nombre", max_length = 100)
    
    def __str__(self):
        return self.nombre
    #Clase Meta
    class Meta:
        verbose_name = "Escuela Profesional" #nombre con el que será visible
        verbose_name_plural = "Escuelas Profesionales" #nombre con el que será visible el plural
        db_table = "EscuelaProfesional" #Tabla asociada