from rest_framework import serializers
from .models import Pocion, Ingrediente

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'origen')

class PocionSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True, read_only=True)

    class Meta:
        model = Pocion
        fields = (
            'id',
            'nombre',
            'precio',
            'descripcion',
            'ingredientes',
            'tamano',
            'bruja'
        )