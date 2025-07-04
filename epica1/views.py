from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, generics
from .serializers import UsuarioSerializer, GroupSerializer, UsuarioVendedorSerializer
from .models import Usuario, Group
from rest_framework.permissions import AllowAny
#ViewSet de Usuario
class UsuarioViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Usuario.
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def get_permissions(self):  
        permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
    
#ViewSet de Group
class GroupViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    def get_permissions(self):
        """
        Asigna permisos dependiendo del método HTTP.
        """
        if self.action == 'list' or self.action == 'retrieve':  # Para GET (ver)
            permission_classes = [permissions.AllowAny]  # Permite a cualquiera ver los datos
        else:  # Para POST, PUT, PATCH, DELETE (editar o agregar)
            permission_classes = [permissions.IsAuthenticated]  # Solo los autenticados pueden modificar

        return [permission() for permission in permission_classes]

class VendedoresViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Endpoint para listar vendedores (solo lectura)
    """
    queryset = Usuario.objects.filter(es_vendedor=True)
    serializer_class = UsuarioVendedorSerializer
    permission_classes = [permissions.AllowAny]