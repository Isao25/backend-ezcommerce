from django.test import TestCase
from epica6.models import OrdenCompra, Detalle, TipoMensaje, TipoSala, SalaChat, Mensaje
from epica1.models import Usuario
from epica4.models import Articulo, Catalogo, Etiqueta
from epica5.models import Marca
from django.utils import timezone

class ModelTests(TestCase):
    def setUp(self):
        self.usuario = Usuario.objects.create(username="testuser", email="test@example.com", nombres="Test", apellido_p="User", apellido_m="Test", celular="123456789", codigo="U123")
        self.marca = Marca.objects.create(id_usuario=self.usuario, nombre="MarcaTest", descripcion="Desc", logo="http://logo.com")
        self.catalogo = Catalogo.objects.get(id_usuario=self.usuario)
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