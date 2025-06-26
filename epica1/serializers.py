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