from rest_framework import serializers
from .models import *

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad
        fields = '__all__'

class EscuelaProfesionalSerializer(serializers.ModelSerializer):
    id_facultad = serializers.IntegerField(source='id_facultad.id')
    class Meta:
        model = EscuelaProfesional
        fields = '__all__'