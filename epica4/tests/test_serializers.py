import pytest
from django.test import TestCase
from epica4.serializers import CatalogoSerializer, ArticuloSerializer, EtiquetaSerializer, ImagenSerializer
from epica4.models import Catalogo, Articulo, Etiqueta, Imagen
from epica2.models import EscuelaProfesional, Facultad
from epica1.models import Usuario

class EtiquetaSerializerTest(TestCase):
    def setUp(self):
        self.etiqueta_data = {
            "nombre": "Prueba",
            "descripcion": "Etiqueta de prueba"
        }

    def test_etiqueta_create(self):
        serializer = EtiquetaSerializer(data=self.etiqueta_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        etiqueta = serializer.save()
        self.assertEqual(etiqueta.nombre, "Prueba")
        self.assertEqual(etiqueta.descripcion, "Etiqueta de prueba")

class CatalogoSerializerTest(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F010", nombre="Facultad de Ingeniería Pruebas", siglas="FIP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="EP010", nombre="Escuela Ingeniería de Prueba")
        self.usuario = Usuario.objects.create_user(
            nombres="Carlos", username="carlos123", email="carlos@test.com",
            id_escuela=self.escuela, password="1234prueba", apellido_p="Gómez", apellido_m="Martínez",
            celular="999999999", codigo="U12345"
        )
        self.catalogo_data = {
            "id_usuario": self.usuario.id,
            "id_marca":None,
            "capacidad_maxima": 15,
            "espacio_ocupado": 0
        }

    def test_catalogo_create(self):
        serializer = CatalogoSerializer(data=self.catalogo_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        catalogo = serializer.save()
        self.assertEqual(catalogo.capacidad_maxima, 15)
        self.assertEqual(catalogo.espacio_ocupado, 0)
        self.assertEqual(catalogo.id_usuario, self.usuario)

class ArticuloSerializerTest(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F010", nombre="Facultad de Ingeniería Pruebas", siglas="FIP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="EP010", nombre="Escuela Ingeniería de Prueba")
        self.usuario = Usuario.objects.create_user(
            nombres="Carlos", username="carlos123", email="carlos@test.com",
            id_escuela=self.escuela, password="1234prueba", apellido_p="Gómez", apellido_m="Martínez",
            celular="999999999", codigo="U12345"
        )
        self.catalogo = Catalogo.objects.create(id_usuario=self.usuario, capacidad_maxima=15, espacio_ocupado=0)
        self.etiqueta = Etiqueta.objects.create(nombre="Prueba", descripcion="Etiqueta de prueba")

    def test_articulo_create(self):
        data = {
            "id_catalogo": self.catalogo.id,
            "nombre": "Articulo de prueba",
            "descripcion": "Este es un artículo de prueba.",
            "precio": 15.7,
            "stock": 50,
            "disponible": True,
            "bloqueado": False,
            "etiquetas": [self.etiqueta.id]
        }
        serializer = ArticuloSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        articulo = serializer.save()
        self.assertEqual(articulo.nombre, "Articulo de prueba")
        self.assertIn(self.etiqueta, articulo.etiquetas.all())

class ImagenSerializerTest(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F010", nombre="Facultad de Ingeniería Pruebas", siglas="FIP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="EP010", nombre="Escuela Ingeniería de Prueba")
        self.usuario = Usuario.objects.create_user(
            nombres="Carlos", username="carlos123", email="carlos@test.com",
            id_escuela=self.escuela, password="1234prueba", apellido_p="Gómez", apellido_m="Martínez",
            celular="999999999", codigo="U12345"
        )
        self.catalogo = Catalogo.objects.create(id_usuario=self.usuario, capacidad_maxima=15, espacio_ocupado=0)
        self.etiqueta = Etiqueta.objects.create(nombre="Prueba", descripcion="Etiqueta de prueba")
        self.articulo = Articulo.objects.create(
            id_catalogo=self.catalogo,
            nombre="Articulo de prueba",
            descripcion="Este es un artículo de prueba.",
            precio=15.7,
            stock=50,
            disponible=True,
            bloqueado=False
        )
        self.articulo.etiquetas.set([self.etiqueta])

    def test_imagen_create(self):
        data = {
            "id_articulo": self.articulo.id,
            "url": "https://image.com"
        }
        serializer = ImagenSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        imagen = serializer.save()
        self.assertEqual(imagen.id_articulo, self.articulo)
        self.assertEqual(imagen.url, "https://image.com")

@pytest.mark.django_db
def test_catalogo_serializer():
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
    data = CatalogoSerializer(cat).data
    assert data['id_usuario'] == usuario.id

@pytest.mark.django_db
def test_articulo_serializer_create():
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