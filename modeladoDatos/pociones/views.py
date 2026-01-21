from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Pocion, Ingrediente, Efecto, Especialidad, Aquelarre, Bruja, Cliente, Pedido, PocionesPedido
from .serializers import PocionSerializer, IngredienteSerializer, EfectoSerializer, EspecialidadSerializer, AquelarreSerializer, BrujaSerializer, ClienteSerializer, PedidoSerializer

class EfectoViewSet(ModelViewSet):
    queryset = Efecto.objects.all()
    serializer_class = EfectoSerializer

class EspecialidadViewSet(ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer

class AquelarreViewSet(ModelViewSet):
    queryset = Aquelarre.objects.all()
    serializer_class = AquelarreSerializer

class BrujaViewSet(ModelViewSet):
    queryset = Bruja.objects.all()
    serializer_class = BrujaSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PocionViewSet(ModelViewSet):
    queryset = Pocion.objects.all()
    serializer_class = PocionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['tamano', 'ingredientes']

class IngredienteViewSet(ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

"""
class PocionesPedidoViewSet(ModelViewSet):
    queryset = PocionesPedido.objects.all()
    serializer_class = PocionesPedidoSerializer
"""