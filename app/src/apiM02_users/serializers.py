# serializers.py
from rest_framework import serializers
from .models import Rol, Ubicacion

class RolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rol
        fields = ('idRol', 'nombre')


class UbicacionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ('ubi_codigo', 'nombre')