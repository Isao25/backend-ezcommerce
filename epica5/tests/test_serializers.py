from django.test import TestCase
from epica5.serializers import MarcaSerializer, PlanSerializer, MembresiaSerializer
from epica5.models import Marca, Plan, Membresia
from epica1.models import Usuario
from epica2.models import EscuelaProfesional, Facultad
from datetime import datetime, timedelta
from django.utils.timezone import make_aware

class MarcaSerializerTest(TestCase):
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


    def test_marca_create(self):
        data = {
            'nombre': 'Marca Serializer',
            'descripcion': 'Descripción desde serializer',
            'logo': 'https://example.com/logo3.png',
            'id_usuario': self.usuario.id
        }
        serializer = MarcaSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        marca = serializer.save()
        self.assertEqual(marca.nombre, 'Marca Serializer')

class PlanSerializerTest(TestCase):
    def test_plan_fields(self):
        plan = Plan.objects.create(
            nombre='Plan Prueba',
            descripcion='Test description',
            espacio_extra=20,
            duracion=3,
            precio=15.0
        )
        serializer = PlanSerializer(plan)
        self.assertEqual(serializer.data['nombre'], 'Plan Prueba')

class MembresiaSerializerTest(TestCase):
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
            nombre='Marca Membresia',
            descripcion='Desc',
            logo='https://example.com/logo4.png'
        )
        self.plan = Plan.objects.create(
            nombre='Plan M',
            descripcion='Desc Plan',
            espacio_extra=50,
            duracion=24,
            precio=199.99
        )

    def test_membresia_serializer(self):
        fecha_final = make_aware(datetime.now() + timedelta(days=30))
        membresia = Membresia.objects.create(id_marca=self.marca, id_plan=self.plan, fecha_final=fecha_final)
        serializer = MembresiaSerializer(membresia)
        self.assertEqual(serializer.data['id_marca'], self.marca.id)
        self.assertEqual(serializer.data['id_plan'], self.plan.id)