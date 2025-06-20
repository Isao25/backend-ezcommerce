from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from epica1.models import Usuario
from epica2.models import Facultad, EscuelaProfesional
from django.contrib.auth.models import Group

class UsuarioViewSetTest(APITestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(
            codigo="F012", nombre="Facultad Test 2", siglas="FT2"
        )
        self.escuela = EscuelaProfesional.objects.create(
            id_facultad=self.facultad, codigo="EP012", nombre="Escuela Test 2"
        )
        self.usuario = Usuario.objects.create_user(
            nombres="Luis",
            username="luis123",
            email="luis@test.com",
            password="testpass"
        )
        self.usuario.id_escuela = self.escuela
        self.usuario.apellido_p = "Perez"
        self.usuario.apellido_m = "Suarez"
        self.usuario.celular = "123456789"
        self.usuario.codigo = "U54321"
        self.usuario.save()

    def test_list_usuarios(self):
        url = "/api/usuarios/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

class GroupViewSetTest(APITestCase):
    def setUp(self):
        self.grupo = Group.objects.create(name="Testers")

    def test_list_grupos(self):
        url = "/api/grupos/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
