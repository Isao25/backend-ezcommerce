from rest_framework import serializers
from .models import *

class ReporteSerializer(serializers.ModelSerializer):
    id_usuario = serializers.IntegerField(source='id_usuario.id')
    class Meta:
        model = Reporte
        fields = '__all__'
