from django.db import models

# Create your models here.


class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombre = models.TextField()
    estado = models.BooleanField(default=True)
    #timestamps = models.DateTimeField()

    def __str__(self):
        return str(self.idRol) + ") " + self.nombre


class Ubicacion(models.Model):
    ubi_codigo = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ubi_codigo) + ") " + self.nombre

class Empleado(models.Model):
    emp_codigo = models.PositiveIntegerField(primary_key=True)
    emp_nombres_apellidos = models.TextField()
    ubi_codigo = models.ForeignKey(Ubicacion, on_delete=models.CASCADE, to_field='ubi_codigo')
    plaza = models.TextField()
    puesto = models.TextField()
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.emp_codigo) + ") " + self.emp_nombres_apellidos