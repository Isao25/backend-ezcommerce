from rest_framework.test import APITestCase
from epica1.models import Usuario
from epica2.models import EscuelaProfesional, Facultad
from epica5.models import Marca, Plan, Membresia
from django.utils import timezone
from datetime import timedelta

class MarcaViewSetTest(APITestCase):
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

        Marca.objects.create(
            id_usuario=self.usuario,
            nombre='Marca API',
            descripcion='Marca creada desde test',
            logo='https://example.com/logo.png'
        )

    def test_list_marcas(self):
        response = self.client.get('/marcas/')
        self.assertEqual(response.status_code, 200)

class PlanViewSetTest(APITestCase):
    def setUp(self):
        Plan.objects.create(
            nombre='Plan API',
            descripcion='Test Plan',
            espacio_extra=30,
            duracion=12,
            precio=50.0
        )

    def test_list_planes(self):
        response = self.client.get('/planes/')
        self.assertEqual(response.status_code, 200)

class MembresiaViewSetTest(APITestCase):
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
        marca = Marca.objects.create(
            id_usuario=self.usuario,
            nombre='Marca Memb',
            descripcion='Marca Desc',
            logo='https://example.com/logo.png'
        )
        plan = Plan.objects.create(
            nombre='Plan Memb',
            descripcion='Plan Desc',
            espacio_extra=100,
            duracion=6,
            precio=100.0
        )
        Membresia.objects.create(
            id_marca=marca,
            id_plan=plan,
            fecha_final=timezone.now() + timedelta(days=180)
        )

    def test_list_membresias(self):
        response = self.client.get('/membresias/')
        self.assertEqual(response.status_code, 200)