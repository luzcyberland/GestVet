from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
<<<<<<< HEAD
    cedula_cliente = models.IntegerField(max_length=100)
=======
    cedula_cliente = models.IntegerField()
>>>>>>> Ajustes
    direccion_cliente = models.CharField(max_length=100)
    telefono_cliente = models.CharField(max_length=100)
    ruc_cliente = models.CharField(max_length=100)
    email_cliente = models.CharField(max_length=100)
     
    def __str__(self):
<<<<<<< HEAD
        return self.nombre_cliente
=======
        return self.nombre_cliente + ' ' + self.apellido_cliente 
>>>>>>> Ajustes
     