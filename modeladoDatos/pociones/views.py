from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Pocion, Ingrediente
from .serializers import PocionSerializer


class PocionViewSet(ModelViewSet):
    queryset = Pocion.objects.all()
    serializer_class = PocionSerializer
