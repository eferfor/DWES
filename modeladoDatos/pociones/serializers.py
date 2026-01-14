from rest_framework import serializers
from .models import Pocion, Ingrediente

class PocionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pocion
        fields = '__all__'