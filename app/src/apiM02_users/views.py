from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets

from .serializers import RolSerializer
from .models import Rol


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all().order_by('-idRol')
    serializer_class = RolSerializer