from django.test import TestCase
from epica1.serializers import UsuarioSerializer, GroupSerializer
from epica1.models import Usuario
from epica2.models import Facultad, EscuelaProfesional
from django.contrib.auth.models import Group

class UsuarioSerializerTest(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(
            codigo="F011", nombre="Facultad Test", siglas="FT"
        )
        self.escuela = EscuelaProfesional.objects.create(
            id_facultad=self.facultad, codigo="EP011", nombre="Escuela Test"
        )
        self.usuario = Usuario.objects.create_user(
            nombres="Ana",
            username="ana123",
            email="ana@test.com",
            password="pass1234"
        )
        self.usuario.id_escuela = self.escuela
        self.usuario.apellido_p = "López"
        self.usuario.apellido_m = "García"
        self.usuario.celular = "987654321"
        self.usuario.codigo = "U98765"
        self.usuario.save()

    def test_usuario_serializer_valido(self):
        serializer = UsuarioSerializer(instance=self.usuario)
        data = serializer.data
        self.assertEqual(data["username"], "ana123")
        self.assertEqual(data["email"], "ana@test.com")

class GroupSerializerTest(TestCase):
    def test_group_serializer_valido(self):
        grupo = Group.objects.create(name="GrupoTest")
        serializer = GroupSerializer(instance=grupo)
        data = serializer.data
        self.assertEqual(data["name"], "GrupoTest")
