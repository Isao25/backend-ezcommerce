import pytest
from django.core.exceptions import ValidationError
from epica4.models import Etiqueta, Catalogo, Articulo, Imagen
from epica1.models import Usuario
from epica5.models import Marca

@pytest.mark.django_db
def test_catalogo_limite_espacio():
    user = Usuario.objects.create(username="user1", password="123")
    catalogo = Catalogo(id_usuario=user, capacidad_maxima=1, espacio_ocupado=2)
    with pytest.raises(ValidationError):
        catalogo.full_clean()

@pytest.mark.django_db
def test_articulo_actualiza_espacio():
    user = Usuario.objects.create(username="user2", password="123")
    catalogo = Catalogo.objects.create(id_usuario=user, capacidad_maxima=2, espacio_ocupado=0)
    etiqueta = Etiqueta.objects.create(nombre="test", descripcion="test")
    articulo = Articulo.objects.create(id_catalogo=catalogo, nombre="test", descripcion="desc", precio=10, stock=1)
    articulo.etiquetas.add(etiqueta)
    assert Catalogo.objects.get(pk=catalogo.pk).espacio_ocupado == 1