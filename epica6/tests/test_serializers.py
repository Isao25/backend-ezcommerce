from django.test import TestCase
from epica6.serializers import OrdenCompraSerializer, DetalleSerializer, TipoMensajeSerializer, TipoSalaSerializer, SalaChatSerializer, MensajeSerializer
from epica1.models import Usuario
from epica4.models import Articulo, Catalogo, Etiqueta
from epica5.models import Marca
from epica6.models import OrdenCompra, Detalle, TipoMensaje, TipoSala, SalaChat, Mensaje

class SerializerTests(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(username="user", email="user@mail.com", nombres="Nombre", apellido_p="Apellido", apellido_m="M", celular="987654321", codigo="U234")
        self.marca = Marca.objects.create(id_usuario=self.usuario, nombre="MarcaTest", descripcion="Desc", logo="http://logo.com")
        self.catalogo = Catalogo.objects.get(id_usuario=self.usuario)
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
