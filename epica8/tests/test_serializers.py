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

        self.usuario = Usuario.objects.create(
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

    def test_reporte_create(self):
        data = {
            'id_usuario': {'id': self.usuario.id},
            'titulo': 'Reporte Serializer',
            'descripcion': 'Descripción desde serializer',
        }

        serializer = ReporteSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        reporte = serializer.save()
        self.assertEqual(reporte.titulo, 'Reporte Serializer')
        