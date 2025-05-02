from rest_framework import serializers
from .models import *

class MarcaSerializer(serializers.ModelSerializer):
    id_usuario = serializers.IntegerField(source='id_usuario.id')

    class Meta:
        model = Marca
        fields = '__all__'

    def create(self, validated_data):
        # Extraer el id del usuario desde los datos validados
        usuario_data = validated_data.pop('id_usuario', None)
        
        # Recuperar el objeto de usuario asociado
        if usuario_data:
            validated_data['id_usuario'] = Usuario.objects.get(id=usuario_data['id'])
        
        # Crear la instancia de Marca
        return super().create(validated_data)

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class MembresiaSerializer(serializers.ModelSerializer):
    id_marca = serializers.IntegerField(source='id_marca.id')
    id_plan = serializers.IntegerField(source='id_plan.id')

    class Meta:
        model = Membresia
        fields = '__all__'
