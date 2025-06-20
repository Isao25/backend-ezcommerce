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
        Marca.objects.create(
            id_usuario=self.usuario,
            nombre='Marca API',
            descripcion='Marca creada desde test',
            logo='https://example.com/logo.png'
        )

    def test_list_marcas(self):
        response = self.client.get('/epica5/marca/')
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
        response = self.client.get('/epica5/plan/')
        self.assertEqual(response.status_code, 200)

class MembresiaViewSetTest(APITestCase):
    def setUp(self):
        usuario = Usuario.objects.create(
            username='usermem', email='usermem@example.com', nombres='Name', apellido_p='Last1', apellido_m='Last2', celular='987654321', codigo='C456'
        )
        marca = Marca.objects.create(
            id_usuario=usuario,
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
        response = self.client.get('/epica5/membresia/')
        self.assertEqual(response.status_code, 200)