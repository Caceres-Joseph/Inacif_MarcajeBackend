from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import RolSerializer, UbicacionSerializer
from .models import Rol, Ubicacion


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all().order_by('-idRol')
    serializer_class = RolSerializer

class UbicacionSerializerViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all().order_by('-ubi_codigo')
    serializer_class = UbicacionSerializer