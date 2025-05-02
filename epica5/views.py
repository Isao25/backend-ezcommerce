from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny
from rest_framework.permissions import BasePermission, SAFE_METHODS

class MarcaViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Marca.
    """
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    filterset_fields = '__all__'

    def get_permissions(self):
        """
        Asigna permisos dependiendo del método HTTP.
        """
        if self.action == 'list' or self.action == 'retrieve':  # Para GET (ver)
            permission_classes = [permissions.AllowAny]  # Permite a cualquiera ver los datos
        else:  # Para POST, PUT, PATCH, DELETE (editar o agregar)
            permission_classes = [permissions.IsAuthenticated]  # Solo los autenticados pueden modificar

        return [permission() for permission in permission_classes]


class PlanViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Plan.
    """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    filterset_fields = '__all__'
    
    def get_permissions(self):
        """
        Asigna permisos dependiendo del método HTTP.
        """
        if self.action == 'list' or self.action == 'retrieve':  # Para GET (ver)
            permission_classes = [permissions.AllowAny]  # Permite a cualquiera ver los datos
        else:  # Para POST, PUT, PATCH, DELETE (editar o agregar)
            permission_classes = [permissions.IsAuthenticated]  # Solo los autenticados pueden modificar

        return [permission() for permission in permission_classes]
    

class MembresiaViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Membresia.
    """
    queryset = Membresia.objects.all()
    serializer_class = MembresiaSerializer
    filterset_fields = '__all__'
    
    def get_permissions(self):
        """
        Asigna permisos dependiendo del método HTTP.
        """
        if self.action == 'list' or self.action == 'retrieve':  # Para GET (ver)
            permission_classes = [permissions.AllowAny]  # Permite a cualquiera ver los datos
        else:  # Para POST, PUT, PATCH, DELETE (editar o agregar)
            permission_classes = [permissions.IsAuthenticated]  # Solo los autenticados pueden modificar

        return [permission() for permission in permission_classes]