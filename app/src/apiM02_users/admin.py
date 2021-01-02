from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Rol, Ubicacion

admin.site.register(Rol)
admin.site.register(Ubicacion)