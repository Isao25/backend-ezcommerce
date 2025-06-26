from django.test import TestCase
from epica1.models import Usuario
from epica2.models import Facultad, EscuelaProfesional
from epica8.models import Reporte

class ReporteModelTests(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(
            codigo="F010",
            nombre="Facultad de Ingeniería Pruebas",
            siglas="FIP"
        )
        self.escuela = EscuelaProfesional.objects.create(
            id_facultad=self.facultad,
            codigo="EP010",
            nombre="Escuela Ingeniería de Prueba"
        )
        self.usuario = Usuario.objects.create_user(
            nombres="Carlos",
            username="carlos123",
            email="carlos@test.com",
            id_escuela=self.escuela,
            password="1234prueba",
            apellido_p="Gómez",
            apellido_m="Martínez",
            celular="999999999",
            codigo="U12345"
        )


        self.reporte = Reporte.objects.create(
            id_usuario = self.usuario,
            titulo = "Reporte N1",
            descripcion = "Se reporta una prueba sobre la prueba de prueba que se prueba."
        )
        self.reporte.save()

    def test_str_reporte(self):
        self.assertEqual(str(self.reporte), "Carlos Gómez Martínez - Reporte N1")

    def test_campos_reporte(self):
        self.assertEqual(self.reporte.titulo, "Reporte N1")
        self.assertEqual(self.reporte.descripcion, "Se reporta una prueba sobre la prueba de prueba que se prueba.")

    def test_relacion_usuario(self):
        self.assertEqual(self.reporte.id_usuario, self.usuario)
