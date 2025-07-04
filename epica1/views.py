from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions, generics
from .serializers import UsuarioSerializer, GroupSerializer, UsuarioVendedorSerializer
from .models import Usuario, Group
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
#ViewSet de Usuario
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    def get_permissions(self):
        if self.action == 'destroy':
            # Permite eliminar si es admin O si es el propio usuario
            permission_classes = [IsAuthenticated]
        elif self.action in ['update', 'partial_update']:
            # Permite actualizar solo si es admin
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        
        # Verifica si es admin o el propio usuario
        if not (request.user.is_staff or request.user == instance):
            return Response(
                {"detail": "No tiene permiso para realizar esta acción."},
                status=status.HTTP_403_FORBIDDEN
            )
            
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def perform_destroy(self, instance):
        # Lógica adicional antes de eliminar (opcional)
        instance.delete()
    
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