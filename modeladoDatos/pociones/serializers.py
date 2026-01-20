from rest_framework import serializers
from .models import Pocion, Ingrediente, Efecto, Especialidad, Aquelarre, Bruja, Cliente, Pedido, PocionesPedido

class EfectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Efecto
        fields = ('id', 'nombre', 'descripcion')

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('id', 'nombre')

class AquelarreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aquelarre
        fields = ('id', 'nombre', 'ubicacion')

class BrujaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bruja
        fields = ('id', 'nombre', 'especialidad', 'aquelarre')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'usuario', 'nombre', 'direccion', 'email', 'telefono', 'fecha_nacimiento')

class IngredienteSerializer(serializers.ModelSerializer):
    # Sólo lectura
    efecto_detalle = EfectoSerializer(
        source="efectos",
        read_only=True,
        many=True
    )

    # Sólo escritura
    efectos = serializers.PrimaryKeyRelatedField(
        queryset=Efecto.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'origen', 'efectos', 'efecto_detalle')

    def create(self, validated_data):
        efectos = validated_data.pop('efectos')
        ingrediente = Ingrediente.objects.create(**validated_data)
        ingrediente.efectos.set(efectos)
        return ingrediente

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

class PocionesPedidoSerializer(serializers.ModelSerializer):
    pocion = serializers.PrimaryKeyRelatedField(queryset=Pocion.objects.all())

    class Meta:
        model = PocionesPedido
        fields = ('pocion', 'cantidad')

class PedidoSerializer(serializers.ModelSerializer):
    items = PocionesPedidoSerializer(many=True)

    class Meta:
        model = Pedido
        fields = ('id', 'cliente', 'fecha', 'items', 'precio_total')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        pedido = Pedido.objects.create(**validated_data)

        for item in items_data:
            PocionesPedido.objects.create(
                pedido=pedido,
                pocion=item['pocion'],
                cantidad=item.get('cantidad', 1)
            )

        return pedido