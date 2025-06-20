from rest_framework.test import APITestCase
from epica1.models import Usuario
from epica2.models import Facultad, EscuelaProfesional
from epica8.models import Reporte
from epica8.serializers import ReporteSerializer
from epica8.views import ReporteViewSet

class ReporteViewSetTest(APITestCase):
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

        Reporte.objects.create(
            id_usuario = self.usuario.id,
            titulo = "Reporte N° 1",
            descripcion = "Se reporta una prueba sobre la prueba de prueba que se prueba."
        )

    def test_list_reportes(self):
        response = self.client.get('/epica8/reporte/')
        self.assertEqual(response.status_code, 200)
