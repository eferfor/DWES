from rest_framework import serializers
from .models import Pocion, Ingrediente

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'origen')

class PocionSerializer(serializers.ModelSerializer):
    ingredientes = serializers.PrimaryKeyRelatedField(queryset=Ingrediente.objects.all(), many=True)

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

    def create(self, validated_data):
        ingredientes = validated_data.pop('ingredientes')
        pocion = Pocion.objects.create(**validated_data)
        pocion.ingredientes.set(ingredientes)
        return pocion