from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from epica1.models import Usuario
from epica6.models import TipoSala, TipoMensaje, SalaChat, OrdenCompra
from epica5.models import Marca

class ViewTests(APITestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create_user(username="testuser", password="pass1234", email="test@mail.com", nombres="Test")
        self.client.force_authenticate(user=self.usuario)
        Marca.objects.create(id_usuario=self.usuario, nombre="M", descripcion="D", logo="http://url.com")
        self.tipo_sala = TipoSala.objects.create(nombre="TS", descripcion="desc")
        self.tipo_mensaje = TipoMensaje.objects.create(nombre="TM", descripcion="desc")
        self.sala = SalaChat.objects.create(nombre="Sala", tipo=self.tipo_sala)
        self.sala.usuarios.add(self.usuario)
        self.orden = OrdenCompra.objects.create(id_usuario=self.usuario)

    def test_list_tipos_sala(self):
        url = reverse("tiposala-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_mensajes(self):
        url = reverse("mensaje-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_ordenes(self):
        url = reverse("ordencompra-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

