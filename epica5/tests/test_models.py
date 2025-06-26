from django.test import TestCase
from epica5.models import Marca, Plan, Membresia
from epica1.models import Usuario
from epica2.models import EscuelaProfesional, Facultad
from django.utils import timezone
from datetime import timedelta

class MarcaModelTest(TestCase):
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

        self.marca = Marca.objects.create(
            id_usuario=self.usuario,
            nombre='Marca Test',
            descripcion='Descripción de prueba',
            logo='https://example.com/logo.png'
        )

    def test_str(self):
        self.assertEqual(str(self.marca), 'Marca Test')

class PlanModelTest(TestCase):
    def setUp(self):
        self.plan = Plan.objects.create(
            nombre='Plan Básico',
            descripcion='Incluye espacio limitado',
            espacio_extra=10,
            duracion=6,
            precio=29.99
        )

    def test_str(self):
        self.assertEqual(str(self.plan), 'Plan Básico')

class MembresiaModelTest(TestCase):
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
        self.marca = Marca.objects.create(
            id_usuario=self.usuario,
            nombre='Otra Marca',
            descripcion='Descripción extendida',
            logo='https://example.com/logo2.png'
        )
        self.plan = Plan.objects.create(
            nombre='Plan Avanzado',
            descripcion='Más beneficios',
            espacio_extra=25,
            duracion=12,
            precio=59.99
        )
        self.membresia = Membresia.objects.create(
            id_marca=self.marca,
            id_plan=self.plan,
            fecha_final=timezone.now() + timedelta(days=365)
        )

    def test_str(self):
        expected = f"{self.membresia.id_marca.nombre} - {self.membresia.id_plan.nombre} : {self.membresia.fecha_inicio}"
        self.assertEqual(str(self.membresia), expected)