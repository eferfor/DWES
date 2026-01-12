from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Pocion, Ingrediente

class PocionListAPIView(APIView):
    def get(self, request):
        pociones = Pocion.objects.all()

        data = []
        for pocion in pociones:

            # Primero saca la lista de ingredientes de cada poción
            ingredientes = pocion.ingredientes.all()
            lista_ingredientes = []
            for ingrediente in ingredientes:
                ing_data = {}
                ing_data['id'] = ingrediente.pk
                ing_data['nombre'] = ingrediente.nombre
                ing_data['origen'] = ingrediente.origen

                lista_ingredientes.append(ing_data)

            # Añade los datos de la poción con la lista de ingredientes
            data.append({
                'id': pocion.pk,
                'nombre': pocion.nombre,
                'precio': pocion.precio,
                'descripcion': pocion.descripcion,
                'ingredientes': lista_ingredientes,
                'tamano': pocion.tamano,
                'bruja': pocion.bruja.pk
            })

        return Response(data)

    # def post(self, request):


class PocionDetailAPIView(APIView):
    def get(self, request, pk):
        pocion = Pocion.objects.get(pk=pk)
        ingredientes = pocion.ingredientes.all()

        lista_ingredientes = []
        for ingrediente in ingredientes:
            ing_data = {
                'id': ingrediente.pk,
                'nombre': ingrediente.nombre,
                'origen': ingrediente.origen,
            }

            lista_ingredientes.append(ing_data)

        data = {
            'id': pocion.pk,
            'nombre': pocion.nombre,
            'precio': pocion.precio,
            'descripcion': pocion.descripcion,
            'ingredientes': lista_ingredientes,
            'tamano': pocion.tamano,
            'bruja': pocion.bruja.pk
        }

        return Response(data)