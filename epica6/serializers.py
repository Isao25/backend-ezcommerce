from rest_framework import serializers
from epica1.models import Usuario
from epica4.models import Articulo
from .models import OrdenCompra, Detalle, TipoSala, TipoMensaje, Mensaje, SalaChat

class OrdenCompraSerializer(serializers.ModelSerializer):
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    class Meta:
        model = OrdenCompra
        fields = '__all__'

class DetalleSerializer(serializers.ModelSerializer):
    id_articulo  = serializers.PrimaryKeyRelatedField(queryset=Articulo.objects.all())
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
    tipo = serializers.PrimaryKeyRelatedField(queryset=TipoSala.objects.all())
    class Meta:
        model = SalaChat
        fields = '__all__'

class MensajeSerializer(serializers.ModelSerializer):
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    tipo =  serializers.PrimaryKeyRelatedField(queryset=TipoMensaje.objects.all())
    id_sala  = serializers.PrimaryKeyRelatedField(queryset=SalaChat.objects.all())
    class Meta:
        model = Mensaje
        fields = '__all__'