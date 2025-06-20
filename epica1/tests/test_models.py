from django.test import TestCase
from epica1.models import Usuario
from epica2.models import Facultad, EscuelaProfesional

class UsuarioModelTest(TestCase):
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
            password="1234prueba"
        )
        self.usuario.id_escuela = self.escuela
        self.usuario.apellido_p = "Gómez"
        self.usuario.apellido_m = "Martínez"
        self.usuario.celular = "999999999"
        self.usuario.codigo = "U12345"
        self.usuario.save()

    def test_creacion_usuario(self):
        self.assertEqual(self.usuario.username, "carlos123")
        self.assertTrue(self.usuario.check_password("1234prueba"))
        self.assertEqual(str(self.usuario), "Carlos Gómez Martínez")

    def test_es_staff_activo(self):
        self.assertTrue(self.usuario.is_active)
        self.assertFalse(self.usuario.is_staff)  # No es superuser

    def test_campos_extra(self):
        self.assertEqual(self.usuario.celular, "999999999")
        self.assertEqual(self.usuario.codigo, "U12345")

    def test_relacion_escuela(self):
        self.assertEqual(self.usuario.id_escuela, self.escuela)

    def test_perm_methods(self):
        self.assertTrue(self.usuario.has_perm(None))
        self.assertTrue(self.usuario.has_module_perms(None))
