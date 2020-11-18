from django.db import models

# Create your models here.


class Rol(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombre = models.TextField()
    estado = models.BooleanField(default=True)
    #timestamps = models.DateTimeField()

    def __str__(self):
        return str(self.idRol) + ") " + self.nombre