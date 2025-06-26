import pytest
from rest_framework.test import APITestCase, APIClient
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


@pytest.fixture
def usuario_autenticado():
    facultad = Facultad.objects.create(codigo="F001", nombre="Facultad Prueba", siglas="FP")
    escuela = EscuelaProfesional.objects.create(id_facultad=facultad, codigo="EP01", nombre="Escuela Prueba")
    usuario = Usuario.objects.create_user(
        nombres="Carlos", username="carlos123", email="carlos@test.com",
        id_escuela=escuela, password="1234prueba",
        apellido_p="Gomez", apellido_m="Martinez", celular="999999999", codigo="U12345"
    )
    client = APIClient()
    client.force_authenticate(user=usuario)
    return client


@pytest.mark.django_db
def test_get_reporte(usuario_autenticado):
    client = usuario_autenticado 
    usuario = Usuario.objects.get(username="carlos123")  

    Reporte.objects.create(
        id_usuario=usuario,
        titulo="Reporte N° 1",
        descripcion="Se reporta una prueba sobre la prueba de prueba que se prueba."
    )

    response = client.get("/reporte/")
    assert response.status_code == 200
