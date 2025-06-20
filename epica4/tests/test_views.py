import pytest
from rest_framework.test import APIClient
from epica4.models import Etiqueta, Catalogo, Articulo
from epica1.models import Usuario

@pytest.mark.django_db
def test_get_etiquetas():
    Etiqueta.objects.create(nombre="E1", descripcion="desc")
    client = APIClient()
    response = client.get("/api/etiquetas/")
    assert response.status_code == 200
    assert len(response.json()) >= 1

@pytest.mark.django_db
def test_create_articulo_view():
    user = Usuario.objects.create_user(username="uview", password="123")
    cat = Catalogo.objects.create(id_usuario=user)
    etiqueta = Etiqueta.objects.create(nombre="vtag", descripcion="desc")

    client = APIClient()
    client.force_authenticate(user=user)
    data = {
        "id_catalogo": cat.id,
        "nombre": "Articulo Test",
        "descripcion": "desc",
        "precio": 30,
        "stock": 5,
        "etiquetas": [etiqueta.id]
    }
    response = client.post("/api/articulos/", data, format='json')
    assert response.status_code == 201