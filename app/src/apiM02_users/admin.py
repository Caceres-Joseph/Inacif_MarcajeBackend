from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Rol, Ubicacion, Empleado

admin.site.register(Rol)
admin.site.register(Ubicacion)
admin.site.register(Empleado)