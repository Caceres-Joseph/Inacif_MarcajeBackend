# serializers.py
from rest_framework import serializers
from .models import Rol

class RolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rol
        fields = ('idRol', 'nombre')