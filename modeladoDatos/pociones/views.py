from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated

from .filters import PocionFilter, EfectoFilter
from .models import Pocion, Ingrediente, Efecto, Especialidad, Aquelarre, Bruja, Cliente, Pedido, PocionesPedido
from .serializers import PocionSerializer, IngredienteSerializer, EfectoSerializer, EspecialidadSerializer, \
    AquelarreSerializer, BrujaSerializer, ClienteSerializer, PedidoSerializer, VerPedidoSerializer


class EfectoViewSet(ModelViewSet):
    queryset = Efecto.objects.all()
    serializer_class = EfectoSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

    filter_backends = [DjangoFilterBackend]
    filterset_class = EfectoFilter

class EspecialidadViewSet(ModelViewSet):
    queryset = Especialidad.objects.all()
    serializer_class = EspecialidadSerializer
    permission_classes = [IsAuthenticated]

class AquelarreViewSet(ModelViewSet):
    queryset = Aquelarre.objects.all()
    serializer_class = AquelarreSerializer
    permission_classes = [IsAuthenticated]

class BrujaViewSet(ModelViewSet):
    queryset = Bruja.objects.all()
    serializer_class = BrujaSerializer
    permission_classes = [IsAuthenticated]

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    # Acción: ver pedidos por cliente
    @action(
        detail=True,
        methods=['get'],
        url_path='pedidos',
        permission_classes=[IsAuthenticated]
    )
    def pedidos(self, request, pk=None):
        usuario = request.user

        try:
            cliente = Cliente.objects.get(pk=pk, usuario=usuario)

        except Cliente.DoesNotExist:
            return Response(
                {"error": "el cliente no existe"}, status=404
            )

        pedidos = Pedido.objects.filter(cliente=cliente)

        if not pedidos:
            return Response(
                {"error": "el cliente no tiene pedidos"}, status=404
            )

        serializer = VerPedidoSerializer(pedidos, many=True)
        return Response(serializer.data)


class PocionViewSet(ModelViewSet):
    queryset = Pocion.objects.all()
    serializer_class = PocionSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_class = PocionFilter
    search_fields = ['nombre', 'descripcion']
    ordering_fields = ['precio']
    ordering = ['id']

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]


class IngredienteViewSet(ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        return [IsAuthenticated()]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['efectos']
    ordering_fields = ['nombre']
    ordering = ['id']


class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]
