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
            nombres="Shamir",
            username="isaoIsao25",
            email="isao25@test.com",
            password="1234prueba",
            id_escuela = self.escuela,
            apellido_p = "Mantquisha",
            apellido_m = "Flowers",
            celular = "999999999",
            codigo = "22200303"
        )
        self.usuario.save()

        self.reporte = Reporte.objects.create(
            id_usuario = self.usuario.id,
            titulo = "Reporte N° 1",
            descripcion = "Se reporta una prueba sobre la prueba de prueba que se prueba."
        )
        self.reporte.save()

    def test_str_reporte(self):
        self.assertEqual(str(self.reporte), "Reporte N° 1")

    def test_campos_reporte(self):
        self.assertEqual(self.reporte.titulo, "Reporte N° 1")
        self.assertEqual(self.reporte.descripcion, "Se reporta una prueba sobre la prueba de prueba que se prueba.")

    def test_relacion_usuario(self):
        self.assertEqual(self.reporte.id_usuario, self.usuario)
