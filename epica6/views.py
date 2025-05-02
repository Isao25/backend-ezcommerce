from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny

class OrdenCompraViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de OrdenCompra.
    """
    queryset = OrdenCompra.objects.all()
    serializer_class = OrdenCompraSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = '__all__'

class DetalleViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Detalle.
    """
    queryset = Detalle.objects.all()
    serializer_class = DetalleSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = '__all__'

class TipoMensajeViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de TipoMensaje.
    """
    queryset = TipoMensaje.objects.all()
    serializer_class = TipoMensajeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = '__all__'

class TipoSalaViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de TipoSala.
    """
    queryset = TipoSala.objects.all()
    serializer_class = TipoSalaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_fields = '__all__'

class SalaChatViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de SalaChat.
    """
    queryset = SalaChat.objects.all()
    serializer_class = SalaChatSerializer
    permission_classes = [permissions.IsAuthenticated]

class MensajeViewSet(viewsets.ModelViewSet):
    """
    API Endpoint para CRUD de Mensaje.
    """
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer
    permission_classes = [permissions.IsAuthenticated]