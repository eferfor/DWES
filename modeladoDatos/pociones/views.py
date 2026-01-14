from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pocion, Ingrediente
from .serializers import PocionSerializer


class PocionListAPIView(APIView):
    def get(self, request):
        pociones = Pocion.objects.all()
        serializer = PocionSerializer(pociones, many=True)
        return Response(serializer.data)

class PocionCreateAPIView(APIView):
    def post(self, request):
        serializer = PocionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)

class PocionDetailAPIView(APIView):
    def get(self, request, pk):
        pocion = Pocion.objects.get(pk=pk)
        serializer = PocionSerializer(pocion)

        return Response(serializer.data)