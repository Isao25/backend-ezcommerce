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


        Reporte.objects.create(
            id_usuario = self.usuario,
            titulo = "Reporte N° 1",
            descripcion = "Se reporta una prueba sobre la prueba de prueba que se prueba."
        )

    '''def test_list_reportes(self):
        response = self.client.get('/reporte/')
        self.assertEqual(response.status_code, 200)'''
