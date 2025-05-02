from rest_framework import serializers
from django.contrib.auth.models import Group, User
from .models import *

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        #lookup_field = 'username' 

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
        #lookup_field = 'name' 