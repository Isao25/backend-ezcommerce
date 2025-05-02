from rest_framework import serializers
from .models import *

class OrdenCompraSerializer(serializers.ModelSerializer):
    id_usuario = serializers.IntegerField(source='id_usuario.id')
    class Meta:
        model = OrdenCompra
        fields = '__all__'

class DetalleSerializer(serializers.ModelSerializer):
    id_articulo = serializers.IntegerField(source='id_articulo.id')
    class Meta:
        model = Detalle
        fields = '__all__'

class TipoSalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSala
        fields = '__all__'

class TipoMensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMensaje
        fields = '__all__'

class SalaChatSerializer(serializers.ModelSerializer):
    tipo = serializers.IntegerField(source='tipo.id')
    class Meta:
        model = SalaChat
        fields = '__all__'

class MensajeSerializer(serializers.ModelSerializer):
    id_usuario = serializers.IntegerField(source='id_usuario.id')
    tipo = serializers.IntegerField(source='tipo.id')
    id_sala = serializers.IntegerField(source='id_sala.id')
    class Meta:
        model = Mensaje
        fields = '__all__'