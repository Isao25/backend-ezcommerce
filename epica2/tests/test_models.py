from django.test import TestCase
from epica2.models import Facultad, EscuelaProfesional

class FacultadModelTest(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(
            codigo="F001",
            nombre="Facultad de Ingeniería de Pruebas",
            siglas="FIP"
        )

    def test_str_facultad(self):
        self.assertEqual(str(self.facultad), "Facultad de Ingeniería de Pruebas (FIP)")

    def test_campos_facultad(self):
        self.assertEqual(self.facultad.codigo, "F001")
        self.assertEqual(self.facultad.nombre, "Facultad de Ingeniería de Pruebas")
        self.assertEqual(self.facultad.siglas, "FIP")

class EscuelaProfesionalModelTest(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(
            codigo="F002",
            nombre="Facultad de Ciencias del Test",
            siglas="FCT"
        )
        self.escuela = EscuelaProfesional.objects.create(
            id_facultad=self.facultad,
            codigo="EP001",
            nombre="Escuela de Pruebas de Biología"
        )

    def test_str_escuela(self):
        self.assertEqual(str(self.escuela), "Escuela de Pruebas de Biología")

    def test_relacion_facultad(self):
        self.assertEqual(self.escuela.id_facultad, self.facultad)