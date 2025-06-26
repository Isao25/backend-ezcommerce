import pytest
from rest_framework.test import APIClient
from epica4.models import Etiqueta, Catalogo, Articulo, Imagen
from epica2.models import EscuelaProfesional, Facultad
from epica1.models import Usuario

@pytest.mark.django_db
def test_get_etiquetas():
    Etiqueta.objects.create(nombre="E1", descripcion="desc")
    client = APIClient()
    response = client.get("/etiquetas/")
    assert response.status_code == 200
    assert len(response.json()) >= 1

@pytest.mark.django_db
def test_get_catalogos():
    facultad = Facultad.objects.create(codigo="F010", nombre="Facultad de Prueba", siglas="FP")
    escuela = EscuelaProfesional.objects.create(id_facultad=facultad, codigo="EP01", nombre="Escuela Prueba")
    usuario = Usuario.objects.create_user(
        nombres="Carlos", username="carlos123", email="carlos@test.com",
        id_escuela=escuela, password="1234prueba", apellido_p="Gómez",
        apellido_m="Martínez", celular="999999999", codigo="U12345"
    )
    Catalogo.objects.create(id_usuario=usuario, capacidad_maxima=10, espacio_ocupado=0)
    client = APIClient()
    response = client.get("/catalogos/")
    assert response.status_code == 200
    assert len(response.json()) >= 1

@pytest.mark.django_db
def test_create_articulo_view():
    facultad = Facultad.objects.create(
        codigo="F010",
        nombre="Facultad de Ingeniería Pruebas",
        siglas="FIP"
    )
    escuela = EscuelaProfesional.objects.create(
        id_facultad=facultad,
        codigo="EP010",
        nombre="Escuela Ingeniería de Prueba"
    )
    usuario = Usuario.objects.create_user(
        nombres="Carlos",
        username="carlos123",
        email="carlos@test.com",
        id_escuela=escuela,
        password="1234prueba",
        apellido_p="Gómez",
        apellido_m="Martínez",
        celular="999999999",
        codigo="U12345"
    )

    cat = Catalogo.objects.create(id_usuario=usuario)
    etiqueta = Etiqueta.objects.create(nombre="vtag", descripcion="desc")

    client = APIClient()
    client.force_authenticate(user=usuario)
    data = {
        "id_catalogo": cat.id,
        "nombre": "Articulo Test",
        "descripcion": "desc",
        "precio": 30,
        "stock": 5,
        "etiquetas": [etiqueta.id]
    }
    response = client.post("/articulos/", data, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_imagenes():
    facultad = Facultad.objects.create(codigo="F010", nombre="Facultad de Prueba", siglas="FP")
    escuela = EscuelaProfesional.objects.create(id_facultad=facultad, codigo="EP01", nombre="Escuela Prueba")
    usuario = Usuario.objects.create_user(
        nombres="Carlos", username="carlos123", email="carlos@test.com",
        id_escuela=escuela, password="1234prueba", apellido_p="Gómez",
        apellido_m="Martínez", celular="999999999", codigo="U12345"
    )
    catalogo = Catalogo.objects.create(id_usuario=usuario, capacidad_maxima=10, espacio_ocupado=0)
    etiqueta = Etiqueta.objects.create(nombre="E1", descripcion="desc")
    articulo = Articulo.objects.create(
        id_catalogo=catalogo, nombre="A1", descripcion="desc", precio=10.0, stock=5, disponible=True, bloqueado=False
    )
    articulo.etiquetas.set([etiqueta])
    Imagen.objects.create(id_articulo=articulo, url="https://img.com/test.png")
    client = APIClient()
    response = client.get("/imagenes/")
    assert response.status_code == 200
    assert len(response.json()) >= 1