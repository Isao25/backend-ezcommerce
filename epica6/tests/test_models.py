from django.test import TestCase
from epica6.models import OrdenCompra, Detalle, TipoMensaje, TipoSala, SalaChat, Mensaje
from epica1.models import Usuario
from epica2.models import EscuelaProfesional, Facultad
from epica4.models import Articulo, Catalogo, Etiqueta
from epica5.models import Marca
from django.utils import timezone

class OrdenCompraModelTest(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F010", nombre="Facultad de Ingeniería Pruebas", siglas="FIP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="EP010", nombre="Escuela Ingeniería de Prueba")
        self.usuario = Usuario.objects.create_user(
            nombres="Carlos", username="carlos123", email="carlos@test.com",
            id_escuela=self.escuela, password="1234prueba",
            apellido_p="Gómez", apellido_m="Martínez", celular="999999999", codigo="U12345"
        )
        self.orden = OrdenCompra.objects.create(id_usuario=self.usuario)

    def test_str_orden_compra(self):
        self.assertIn(self.usuario.nombres, str(self.orden))

    def test_campos_orden(self):
        self.assertEqual(self.orden.id_usuario, self.usuario)


class DetalleModelTest(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F010", nombre="Facultad de Ingeniería Pruebas", siglas="FIP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="EP010", nombre="Escuela Ingeniería de Prueba")
        self.usuario = Usuario.objects.create_user(
            nombres="Carlos", username="carlos123", email="carlos@test.com",
            id_escuela=self.escuela, password="1234prueba",
            apellido_p="Gómez", apellido_m="Martínez", celular="999999999", codigo="U12345"
        )
        self.catalogo = Catalogo.objects.create(id_usuario=self.usuario, capacidad_maxima=10, espacio_ocupado=0)
        self.articulo = Articulo.objects.create(
            id_catalogo=self.catalogo, nombre="Artículo", descripcion="desc", precio=10.0,
            stock=5, disponible=True, bloqueado=False
        )
        self.orden = OrdenCompra.objects.create(id_usuario=self.usuario)
        self.detalle = Detalle.objects.create(id_articulo=self.articulo, id_orden=self.orden, cantidad=3)

    def test_str_detalle(self):
        self.assertIn("Detalle de Artículo", str(self.detalle))

    def test_clean_valid(self):
        self.assertEqual(self.detalle.cantidad, 3)

    def test_clean_stock_0(self):
        self.articulo.stock = 0
        self.articulo.save()
        detalle = Detalle(id_articulo=self.articulo, id_orden=self.orden, cantidad=2)
        detalle.full_clean()
        detalle.save()
        self.assertEqual(detalle.cantidad, 0)

class TipoMensajeModelTest(TestCase):
    def setUp(self):
        self.tipo = TipoMensaje.objects.create(nombre="Texto", descripcion="Mensaje de texto")

    def test_str_tipo_mensaje(self):
        self.assertEqual(str(self.tipo), "Texto")

    def test_campos_tipo_mensaje(self):
        self.assertEqual(self.tipo.descripcion, "Mensaje de texto")


class TipoSalaModelTest(TestCase):
    def setUp(self):
        self.tipo = TipoSala.objects.create(nombre="Pública", descripcion="Sala abierta")

    def test_str_tipo_sala(self):
        self.assertEqual(str(self.tipo), "Pública")

    def test_campos_tipo_sala(self):
        self.assertEqual(self.tipo.descripcion, "Sala abierta")


class SalaChatModelTest(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F010", nombre="Facultad de Ingeniería Pruebas", siglas="FIP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="EP010", nombre="Escuela Ingeniería de Prueba")
        self.usuario = Usuario.objects.create_user(
            nombres="Carlos", username="carlos123", email="carlos@test.com",
            id_escuela=self.escuela, password="1234prueba",
            apellido_p="Gómez", apellido_m="Martínez", celular="999999999", codigo="U12345"
        )
        self.tipo = TipoSala.objects.create(nombre="Privada", descripcion="Sala privada")
        self.sala = SalaChat.objects.create(nombre="Chat test", tipo=self.tipo)
        self.sala.usuarios.add(self.usuario)

    def test_str_sala_chat(self):
        self.assertIn("-", str(self.sala))

    def test_campos_sala(self):
        self.assertEqual(self.sala.tipo, self.tipo)
        self.assertIn(self.usuario, self.sala.usuarios.all())


class MensajeModelTest(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F010", nombre="Facultad de Ingeniería Pruebas", siglas="FIP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="EP010", nombre="Escuela Ingeniería de Prueba")
        self.usuario = Usuario.objects.create_user(
            nombres="Carlos", username="carlos123", email="carlos@test.com",
            id_escuela=self.escuela, password="1234prueba",
            apellido_p="Gómez", apellido_m="Martínez", celular="999999999", codigo="U12345"
        )
        self.tipo = TipoMensaje.objects.create(nombre="Texto", descripcion="Mensaje de texto")
        self.sala_tipo = TipoSala.objects.create(nombre="Pública", descripcion="Libre")
        self.sala = SalaChat.objects.create(nombre="Sala Test", tipo=self.sala_tipo)
        self.sala.usuarios.add(self.usuario)
        self.mensaje = Mensaje.objects.create(id_usuario=self.usuario, tipo=self.tipo, id_sala=self.sala, mensaje="Hola")

    def test_str_mensaje(self):
        self.assertIn("Carlos", str(self.mensaje))

    def test_campos_mensaje(self):
        self.assertEqual(self.mensaje.mensaje, "Hola")
        self.assertEqual(self.mensaje.id_usuario, self.usuario)
        self.assertEqual(self.mensaje.id_sala, self.sala)
        self.assertEqual(self.mensaje.tipo, self.tipo)

class ModelTests(TestCase):
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

        self.marca = Marca.objects.create(id_usuario=self.usuario, nombre="MarcaTest", descripcion="Desc", logo="http://logo.com")
        self.catalogo = Catalogo.objects.filter(id_usuario=self.usuario).first() #.get(id_usuario=self.usuario)
        self.etiqueta = Etiqueta.objects.create(nombre="Etiqueta", descripcion="desc")
        self.articulo = Articulo.objects.create(id_catalogo=self.catalogo, nombre="Articulo", descripcion="Desc", precio=10.0, stock=5)
        self.articulo.etiquetas.add(self.etiqueta)
        self.orden = OrdenCompra.objects.create(id_usuario=self.usuario)
        self.tipo_sala = TipoSala.objects.create(nombre="Publica", descripcion="Public")
        self.tipo_mensaje = TipoMensaje.objects.create(nombre="Texto", descripcion="Mensaje texto")
        self.sala = SalaChat.objects.create(nombre="Chat 1", tipo=self.tipo_sala)
        self.sala.usuarios.add(self.usuario)

    def test_detalle_save(self):
        detalle = Detalle.objects.create(id_articulo=self.articulo, id_orden=self.orden, cantidad=3)
        self.assertEqual(detalle.cantidad, 3)

    def test_mensaje_creation(self):
        msg = Mensaje.objects.create(id_usuario=self.usuario, tipo=self.tipo_mensaje, id_sala=self.sala, mensaje="Hola")
        self.assertEqual(msg.id_usuario, self.usuario)