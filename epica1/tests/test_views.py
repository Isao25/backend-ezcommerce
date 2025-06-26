from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from epica1.models import Usuario
from epica2.models import Facultad, EscuelaProfesional
from django.contrib.auth.models import Group

class UsuarioViewSetTest(APITestCase):
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

    def test_list_usuarios(self):
        url = "/usuarios/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

class GroupViewSetTest(APITestCase):
    def setUp(self):
        self.grupo = Group.objects.create(name="Testers")

    def test_list_grupos(self):
        url = "/roles/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
