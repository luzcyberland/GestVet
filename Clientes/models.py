from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    cedula_cliente = models.IntegerField()
    direccion_cliente = models.CharField(max_length=100)
    telefono_cliente = models.CharField(max_length=100)
    ruc_cliente = models.CharField(max_length=100)
    email_cliente = models.CharField(max_length=100)
     
    def __str__(self):
        return self.nombre_cliente + ' ' + self.apellido_cliente 
     