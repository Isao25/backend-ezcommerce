from rest_framework import serializers
from .models import Reporte
from epica1.models import Usuario

class ReporteSerializer(serializers.ModelSerializer):
    id_usuario = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all())
    class Meta:
        model = Reporte
        fields = '__all__'
