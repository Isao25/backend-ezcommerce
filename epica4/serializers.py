from rest_framework import serializers
from .models import Etiqueta, Catalogo, Articulo, Imagen
from epica5.models import Marca

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'


class CatalogoSerializer(serializers.ModelSerializer):
    id_usuario = serializers.IntegerField(source='id_usuario.id')
    id_marca = serializers.SerializerMethodField()

    class Meta:
        model = Catalogo
        fields = '__all__'

    def get_id_marca(self, obj):
        # Verifica si 'id_marca' es None y maneja el caso.
        return obj.id_marca.id if obj.id_marca else None
    
    def get_nombre_marca(self, obj):
        return obj.id_catalogo.id_marca.nombre if obj.id_catalogo.id_marca else None
    
    

class ArticuloSerializer(serializers.ModelSerializer):    
    id_catalogo = serializers.PrimaryKeyRelatedField(queryset=Catalogo.objects.all())  # Directamente relacionado
    id_marca = serializers.SerializerMethodField()
    etiquetas = serializers.PrimaryKeyRelatedField(queryset=Etiqueta.objects.all(), many=True)  # Maneja ManyToMany

    class Meta:
        model = Articulo
        fields = '__all__'
        
    def get_id_marca(self, obj):
        return obj.id_catalogo.id_marca.id if obj.id_catalogo.id_marca else None

    def get_nombre_marca(self, obj):
        return obj.id_catalogo.id_marca.nombre if obj.id_catalogo.id_marca else None

    def create(self, validated_data):
        # Extrae etiquetas del validated_data
        etiquetas_data = validated_data.pop('etiquetas', [])
        # Crea el artículo sin etiquetas
        articulo = Articulo.objects.create(**validated_data)
        # Asigna las etiquetas al artículo
        articulo.etiquetas.set(etiquetas_data)
        return articulo

    def update(self, instance, validated_data):
        # Extrae etiquetas del validated_data
        etiquetas_data = validated_data.pop('etiquetas', [])
        # Actualiza los campos del artículo
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        # Actualiza las etiquetas del artículo
        instance.etiquetas.set(etiquetas_data)
        return instance



class ImagenSerializer(serializers.ModelSerializer):    
    id_articulo = serializers.IntegerField(source='id_articulo.id')

    class Meta:
        model = Imagen
        fields = '__all__'

    def create(self, validated_data):
        articulo_id = validated_data.pop('id_articulo')['id']
        
        try:
            from .models import Articulo  
            articulo = Articulo.objects.get(id=articulo_id)            
            imagen = Imagen.objects.create(
                id_articulo=articulo,
                **validated_data
            )
            return imagen
            
        except Articulo.DoesNotExist:
            raise serializers.ValidationError({"id_articulo": "El artículo especificado no existe"})
    
    def update(self, instance, validated_data):
        if 'id_articulo' in validated_data:
            articulo_id = validated_data.pop('id_articulo')['id']
            try:
                from .models import Articulo
                articulo = Articulo.objects.get(id=articulo_id)
                instance.id_articulo = articulo
            except Articulo.DoesNotExist:
                raise serializers.ValidationError({"id_articulo": "El artículo especificado no existe"})

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance