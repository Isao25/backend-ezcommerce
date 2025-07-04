from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import Usuario
#Serializer de Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario #Clase que será serializada 
        fields = '__all__'
#Serializer de Group
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group #Clase que será serializada 
        fields = '__all__'

class UsuarioVendedorSerializer(serializers.ModelSerializer):
    escuela = serializers.CharField(source='id_escuela.nombre')  # Ejemplo para mostrar el nombre de la escuela
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'nombres', 'apellido_p', 'apellido_m', 'email', 'escuela', 'celular', 'codigoqr']