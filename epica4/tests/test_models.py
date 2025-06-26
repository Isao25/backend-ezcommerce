import pytest
from django.test import TestCase
from django.core.exceptions import ValidationError
from epica4.models import Etiqueta, Catalogo, Articulo, Imagen
from epica1.models import Usuario
from epica2.models import EscuelaProfesional, Facultad
from epica5.models import Marca

class EtiquetaModelTest(TestCase):
    def setUp(self):
        self.etiqueta = Etiqueta.objects.create(
            nombre="Prueba",
            descripcion="Etiqueta de prueba"
        )

    def test_str_etiqueta(self):
        self.assertEqual(str(self.etiqueta), "Prueba")

    def test_campos_etiqueta(self):
        self.assertEqual(self.etiqueta.nombre, "Prueba")
        self.assertEqual(self.etiqueta.descripcion, "Etiqueta de prueba")

class CatalogoModelTest(TestCase):
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

        self.catalogo = Catalogo.objects.create(
            id_usuario=self.usuario,
            id_marca=None, 
            capacidad_maxima=15, 
            espacio_ocupado=0
        )

    def test_str_catalogo(self):
        self.assertEqual(str(self.catalogo), 'Catálogo de ' + self.usuario.nombres + ' ' + self.usuario.apellido_p + ' ' + self.usuario.apellido_m)

    def test_campos_catalogo(self):
        self.assertEqual(self.catalogo.id_usuario, self.usuario)
        self.assertEqual(self.catalogo.capacidad_maxima, 15)
        self.assertEqual(self.catalogo.espacio_ocupado, 0)

class ArticuloModelTest(TestCase):
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

        self.catalogo = Catalogo.objects.create(
            id_usuario=self.usuario,
            id_marca=None, 
            capacidad_maxima=15, 
            espacio_ocupado=0
        )

        self.etiqueta = Etiqueta.objects.create(
            nombre="Prueba",
            descripcion="Etiqueta de prueba"
        )

        self.articulo = Articulo.objects.create(
            id_catalogo=self.catalogo,
            id_marca=None,
            nombre="Articulo de prueba",
            descripcion="Este es un artículo de prueba.",
            precio=15.7,
            stock=50,
            disponible=True,
            bloqueado=False
        )
        self.articulo.etiquetas.set([self.etiqueta])

    def test_str_articulo(self):
        self.assertEqual(str(self.articulo), "Articulo de prueba")

    def test_campos_articulo(self):
        self.assertEqual(self.articulo.id_catalogo, self.catalogo)
        self.assertEqual(self.articulo.id_marca, None)
        self.assertEqual(self.articulo.nombre,  "Articulo de prueba")
        self.assertEqual(self.articulo.descripcion,  "Este es un artículo de prueba.")
        self.assertEqual(self.articulo.precio, 15.7)
        self.assertEqual(self.articulo.stock, 50)
        self.assertIn(self.etiqueta, self.articulo.etiquetas.all())
        self.assertEqual(self.articulo.disponible, True)
        self.assertEqual(self.articulo.bloqueado, False) 

 
class ImagenModelTest(TestCase):
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
        
        self.catalogo = Catalogo.objects.create(
            id_usuario=self.usuario,
            id_marca=None, 
            capacidad_maxima=15, 
            espacio_ocupado=0
        )

        self.etiqueta = Etiqueta.objects.create(
            nombre="Prueba",
            descripcion="Etiqueta de prueba"
        )

        self.articulo = Articulo.objects.create(
            id_catalogo=self.catalogo,
            id_marca=None,
            nombre="Articulo de prueba",
            descripcion="Este es un artículo de prueba.",
            precio=15.7,
            stock=50,
            disponible=True,
            bloqueado=False
        )

        self.articulo.etiquetas.set([self.etiqueta])
        self.imagen = Imagen.objects.create(
            id_articulo = self.articulo,
            url = "https://image.com"
        )
    
    def test_str_imagen(self):
        self.assertEqual(str(self.imagen), self.articulo.nombre)

    def test_campos_imagen(self):
        self.assertEqual(self.imagen.id_articulo, self.articulo)
        self.assertEqual(self.imagen.url, "https://image.com")

@pytest.mark.django_db
def test_catalogo_limite_espacio():
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
    
    catalogo = Catalogo(id_usuario=usuario, capacidad_maxima=1, espacio_ocupado=2)
    with pytest.raises(ValidationError):
        catalogo.full_clean()

@pytest.mark.django_db
def test_articulo_actualiza_espacio():
    facultad2 = Facultad.objects.create(
            codigo="F010",
            nombre="Facultad de Ingeniería Pruebas",
            siglas="FIP"
    )
    escuela2 = EscuelaProfesional.objects.create(
        id_facultad=facultad2,
        codigo="EP010",
        nombre="Escuela Ingeniería de Prueba"
    )
    usuario2 = Usuario.objects.create_user(
        nombres="Carlos",
        username="carlos123",
        email="carlos@test.com",
        id_escuela=escuela2,
        password="1234prueba",
        apellido_p="Gómez",
        apellido_m="Martínez",
        celular="999999999",
        codigo="U12345"
    )

    catalogo = Catalogo.objects.create(id_usuario=usuario2, capacidad_maxima=2, espacio_ocupado=0)
    etiqueta = Etiqueta.objects.create(nombre="test", descripcion="test")
    articulo = Articulo.objects.create(id_catalogo=catalogo, nombre="test", descripcion="desc", precio=10, stock=1)
    articulo.etiquetas.add(etiqueta)
    assert Catalogo.objects.get(pk=catalogo.pk).espacio_ocupado == 1