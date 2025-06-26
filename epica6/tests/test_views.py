from rest_framework.test import APITestCase, APIClient
import pytest
from rest_framework import status
from django.urls import reverse
from epica1.models import Usuario
from epica2.models import Facultad, EscuelaProfesional
from epica6.models import TipoSala, TipoMensaje, SalaChat, OrdenCompra, Detalle, Mensaje
from epica5.models import Marca
from epica4.models import Articulo, Catalogo

class ViewTests(APITestCase):
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

        self.client.force_authenticate(user=self.usuario)
        Marca.objects.create(id_usuario=self.usuario, nombre="M", descripcion="D", logo="http://url.com")
        self.tipo_sala = TipoSala.objects.create(nombre="TS", descripcion="desc")
        self.tipo_mensaje = TipoMensaje.objects.create(nombre="TM", descripcion="desc")
        self.sala = SalaChat.objects.create(nombre="Sala", tipo=self.tipo_sala)
        self.sala.usuarios.add(self.usuario)
        self.orden = OrdenCompra.objects.create(id_usuario=self.usuario)


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
def test_get_ordencompra(usuario_autenticado):
    OrdenCompra.objects.create(id_usuario=Usuario.objects.first())
    response = usuario_autenticado.get("/ordencompra/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_detalle(usuario_autenticado):
    articulo = Articulo.objects.create(
        id_catalogo=Catalogo.objects.create(id_usuario=Usuario.objects.first(), capacidad_maxima=10, espacio_ocupado=0),
        nombre="Artículo Test", descripcion="desc", precio=10, stock=3, disponible=True, bloqueado=False
    )
    orden = OrdenCompra.objects.create(id_usuario=Usuario.objects.first())
    Detalle.objects.create(id_articulo=articulo, id_orden=orden, cantidad=2)
    response = usuario_autenticado.get("/detalle/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_tipomensaje(usuario_autenticado):
    TipoMensaje.objects.create(nombre="Texto", descripcion="desc")
    response = usuario_autenticado.get("/tipoMensaje/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_tiposala(usuario_autenticado):
    TipoSala.objects.create(nombre="Pública", descripcion="desc")
    response = usuario_autenticado.get("/tipoSala/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_salas(usuario_autenticado):
    tipo = TipoSala.objects.create(nombre="Pública", descripcion="desc")
    sala = SalaChat.objects.create(nombre="Sala 1", tipo=tipo)
    sala.usuarios.add(Usuario.objects.first())
    response = usuario_autenticado.get("/salaChat/")
    assert response.status_code == 200

@pytest.mark.django_db
def test_get_mensajes(usuario_autenticado):
    tipo = TipoMensaje.objects.create(nombre="Texto", descripcion="desc")
    sala = SalaChat.objects.create(nombre="Sala 1", tipo=TipoSala.objects.create(nombre="Pública", descripcion="desc"))
    sala.usuarios.add(Usuario.objects.first())
    Mensaje.objects.create(id_usuario=Usuario.objects.first(), tipo=tipo, id_sala=sala, mensaje="Hola")
    response = usuario_autenticado.get("/mensaje/")
    assert response.status_code == 200


