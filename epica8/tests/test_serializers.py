from django.test import TestCase
from epica1.models import Usuario
from epica2.models import Facultad, EscuelaProfesional
from epica8.models import Reporte
from epica8.serializers import ReporteSerializer

class ReporteSerializerTest(TestCase):
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


    def test_reporte_create(self):
        data = {
            'id_usuario': self.usuario.id,
            'titulo': 'Reporte Serializer',
            'descripcion': 'Descripción desde serializer',
        }

        serializer = ReporteSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        reporte = serializer.save()
        self.assertEqual(reporte.titulo, 'Reporte Serializer')
        