from django.test import TestCase
from epica6.serializers import OrdenCompraSerializer, DetalleSerializer, TipoMensajeSerializer, TipoSalaSerializer, SalaChatSerializer, MensajeSerializer
from epica1.models import Usuario
from epica4.models import Articulo, Catalogo, Etiqueta
from epica5.models import Marca
from epica2.models import Facultad, EscuelaProfesional
from epica6.models import OrdenCompra, Detalle, TipoMensaje, TipoSala, SalaChat, Mensaje

class OrdenCompraSerializerTests(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F001", nombre="Facultad Prueba", siglas="FP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="E001", nombre="Escuela Prueba")
        self.usuario = Usuario.objects.create_user(username="user1", password="pass", email="a@a.com", nombres="Carlos", apellido_p="Perez", apellido_m="Sanchez", celular="999999999", codigo="U123", id_escuela=self.escuela)

    def test_orden_compra_serializer(self):
        data = {"id_usuario": self.usuario.id}
        serializer = OrdenCompraSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        orden = serializer.save()
        self.assertEqual(orden.id_usuario, self.usuario)


class DetalleSerializerTests(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F001", nombre="Facultad Prueba", siglas="FP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="E001", nombre="Escuela Prueba")
        self.usuario = Usuario.objects.create_user(username="user1", password="pass", email="a@a.com", nombres="Carlos", apellido_p="Perez", apellido_m="Sanchez", celular="999999999", codigo="U123", id_escuela=self.escuela)
        self.catalogo = Catalogo.objects.create(id_usuario=self.usuario, capacidad_maxima=10, espacio_ocupado=0)
        self.articulo = Articulo.objects.create(id_catalogo=self.catalogo, nombre="Articulo Test", descripcion="Desc", precio=10.0, stock=5)
        self.orden = OrdenCompra.objects.create(id_usuario=self.usuario)

    def test_detalle_serializer(self):
        data = {"id_articulo": self.articulo.id, "id_orden": self.orden.id, "cantidad": 3}
        serializer = DetalleSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        detalle = serializer.save()
        self.assertEqual(detalle.cantidad, 3)


class TipoMensajeSerializerTests(TestCase):
    def test_tipo_mensaje_serializer(self):
        data = {"nombre": "Texto", "descripcion": "Mensaje de texto"}
        serializer = TipoMensajeSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        tipo = serializer.save()
        self.assertEqual(tipo.nombre, "Texto")


class TipoSalaSerializerTests(TestCase):
    def test_tipo_sala_serializer(self):
        data = {"nombre": "Pública", "descripcion": "Sala pública"}
        serializer = TipoSalaSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        tipo = serializer.save()
        self.assertEqual(tipo.nombre, "Pública")


class SalaChatSerializerTests(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F001", nombre="Facultad Prueba", siglas="FP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="E001", nombre="Escuela Prueba")
        self.usuario = Usuario.objects.create_user(username="user1", password="pass", email="a@a.com", nombres="Carlos", apellido_p="Perez", apellido_m="Sanchez", celular="999999999", codigo="U123", id_escuela=self.escuela)
        self.tipo_sala = TipoSala.objects.create(nombre="Pública", descripcion="Sala pública")

    def test_sala_chat_serializer(self):
        data = {"nombre": "Chat Test", "tipo": self.tipo_sala.id, "usuarios": [self.usuario.id]}
        serializer = SalaChatSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        sala = serializer.save()
        self.assertEqual(sala.nombre, "Chat Test")


class MensajeSerializerTests(TestCase):
    def setUp(self):
        self.facultad = Facultad.objects.create(codigo="F001", nombre="Facultad Prueba", siglas="FP")
        self.escuela = EscuelaProfesional.objects.create(id_facultad=self.facultad, codigo="E001", nombre="Escuela Prueba")
        self.usuario = Usuario.objects.create_user(username="user1", password="pass", email="a@a.com", nombres="Carlos", apellido_p="Perez", apellido_m="Sanchez", celular="999999999", codigo="U123", id_escuela=self.escuela)
        self.tipo = TipoMensaje.objects.create(nombre="Texto", descripcion="Texto plano")
        self.tipo_sala = TipoSala.objects.create(nombre="Pública", descripcion="Sala pública")
        self.sala = SalaChat.objects.create(nombre="Sala Test", tipo=self.tipo_sala)
        self.sala.usuarios.set([self.usuario])

    def test_mensaje_serializer(self):
        data = {
            "id_usuario": self.usuario.id,
            "tipo": self.tipo.id,
            "id_sala": self.sala.id,
            "mensaje": "Hola mundo",
            "url": ""
        }
        serializer = MensajeSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        msg = serializer.save()
        self.assertEqual(msg.mensaje, "Hola mundo")


class SerializerTests(TestCase):
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
        self.catalogo = Catalogo.objects.filter(id_usuario=self.usuario).first()
        self.etiqueta = Etiqueta.objects.create(nombre="Etiqueta", descripcion="desc")
        self.articulo = Articulo.objects.create(id_catalogo=self.catalogo, nombre="Articulo", descripcion="Desc", precio=10.0, stock=5)
        self.articulo.etiquetas.add(self.etiqueta)
        self.orden = OrdenCompra.objects.create(id_usuario=self.usuario)
        self.tipo_sala = TipoSala.objects.create(nombre="Privada", descripcion="Sala privada")
        self.tipo_mensaje = TipoMensaje.objects.create(nombre="Archivo", descripcion="Archivos")
        self.sala = SalaChat.objects.create(nombre="Sala1", tipo=self.tipo_sala)
        self.sala.usuarios.add(self.usuario)

    def test_orden_serializer(self):
        data = OrdenCompraSerializer(instance=self.orden).data
        self.assertEqual(data["id_usuario"], self.usuario.id)

    def test_detalle_serializer(self):
        detalle = Detalle.objects.create(id_articulo=self.articulo, id_orden=self.orden, cantidad=2)
        data = DetalleSerializer(instance=detalle).data
        self.assertEqual(data["id_articulo"], self.articulo.id)

    def test_mensaje_serializer(self):
        mensaje = Mensaje.objects.create(id_usuario=self.usuario, tipo=self.tipo_mensaje, id_sala=self.sala, mensaje="Hola")
        data = MensajeSerializer(instance=mensaje).data
        self.assertEqual(data["mensaje"], "Hola")
