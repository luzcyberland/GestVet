from django.db import models
from django.contrib.auth.models import AbstractUser
from Roles.models import Rol

#id:number
#nombre:String
#apellido:String
#cedula:number
#direccion:String
#telefono:String
#correo:String

class Usuario(AbstractUser):
    cedula = models.IntegerField(default=0)
    id_rol = models.ForeignKey(Rol, on_delete=models.DO_NOTHING, default=1)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
    

