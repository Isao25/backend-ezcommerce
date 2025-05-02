from django.db import models

class Facultad(models.Model):
    codigo = models.CharField("Código", max_length = 10, unique = True)
    nombre = models.CharField("Nombre", max_length = 100)
    siglas = models.CharField("Siglas", max_length = 20)
    def __str__(self):
        return self.nombre + ' ('+ self.siglas +')'
    
    class Meta:
        verbose_name = "Facultad"
        verbose_name_plural = "Facultades"
        db_table = "Facultad"

class EscuelaProfesional(models.Model):
    id_facultad = models.ForeignKey(Facultad, on_delete = models.CASCADE, verbose_name = "Facultad")
    codigo = models.CharField("Código", max_length = 10, unique = True)
    nombre = models.CharField("Nombre", max_length = 100)
    
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name = "Escuela Profesional"
        verbose_name_plural = "Escuelas Profesionales"
        db_table = "EscuelaProfesional"