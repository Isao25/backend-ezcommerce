import pytest
from epica4.serializers import CatalogoSerializer, ArticuloSerializer, EtiquetaSerializer, ImagenSerializer
from epica4.models import Catalogo, Articulo, Etiqueta, Imagen
from epica1.models import Usuario

@pytest.mark.django_db
def test_catalogo_serializer():
    user = Usuario.objects.create(username="u1", password="123")
    cat = Catalogo.objects.create(id_usuario=user)
    data = CatalogoSerializer(cat).data
    assert data['id_usuario'] == user.id

@pytest.mark.django_db
def test_articulo_serializer_create():
    user = Usuario.objects.create(username="u2", password="123")
    cat = Catalogo.objects.create(id_usuario=user)
    etiqueta = Etiqueta.objects.create(nombre="e1", descripcion="d")
    data = {
        "id_catalogo": cat.id,
        "nombre": "A1",
        "descripcion": "test",
        "precio": 50,
        "stock": 1,
        "etiquetas": [etiqueta.id]
    }
    serializer = ArticuloSerializer(data=data)
    assert serializer.is_valid(), serializer.errors
    articulo = serializer.save()
    assert articulo.nombre == "A1"