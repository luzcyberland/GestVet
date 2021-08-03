from django.db import models

# Clase Rol.

class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol  = models.CharField(max_length=100)
    estado = models.CharField(max_length= 100)

    def __str__(self):
        return self.nombre_rol
