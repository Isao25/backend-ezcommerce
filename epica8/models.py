from django.db import models
from epica1.models import Usuario

class Reporte(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Autor")
    titulo = models.CharField("Titulo", max_length=30)
    descripcion = models.TextField("Descripción")
    fecha_reporte = models.DateTimeField("Fecha del Reporte", auto_now_add=True)

    def __str__(self):
        return self.id_usuario.__str__() + " - " + self.titulo
    
    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
        db_table = "Reporte"

 
