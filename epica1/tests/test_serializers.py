from django.test import TestCase
from epica1.serializers import UsuarioSerializer, GroupSerializer
from epica1.models import Usuario
from epica2.models import Facultad, EscuelaProfesional
from django.contrib.auth.models import Group

class UsuarioSerializerTest(TestCase):
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

    def test_usuario_serializer_valido(self):
        serializer = UsuarioSerializer(instance=self.usuario)
        data = serializer.data
        self.assertEqual(data["username"], "carlos123")
        self.assertEqual(data["email"], "carlos@test.com")

class GroupSerializerTest(TestCase):
    def test_group_serializer_valido(self):
        grupo = Group.objects.create(name="GrupoTest")
        serializer = GroupSerializer(instance=grupo)
        data = serializer.data
        self.assertEqual(data["name"], "GrupoTest")
