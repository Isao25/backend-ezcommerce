from rest_framework import serializers
from .models import Facultad, EscuelaProfesional
#Serializer de Facultad
class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultad #Clase que será serializada 
        fields = '__all__'
#Serializer de EscuelaProfesional
class EscuelaProfesionalSerializer(serializers.ModelSerializer):
    id_facultad = serializers.IntegerField(source='id_facultad.id')
    class Meta:
        model = EscuelaProfesional #Clase que será serializada 
        fields = '__all__'