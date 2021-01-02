from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
# views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import RolSerializer, UbicacionSerializer
from .models import Rol, Ubicacion

# Functions
from .features.apiRest_Inacif import actualizarUbicaciones


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all().order_by('-idRol')
    serializer_class = RolSerializer


class UbicacionSerializerViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all().order_by('-ubi_codigo')
    serializer_class = UbicacionSerializer


class UbicacionSerializerViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all().order_by('-ubi_codigo')
    serializer_class = UbicacionSerializer


# Consumiendo api del INACIF
class actualizar_ubicaciones(APIView):
    def get(self, request, format=None):
        my_result=actualizarUbicaciones.actualizar()
        return JsonResponse(data={"my_return_data": my_result})