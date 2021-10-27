from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=100)
    direccion_proveedor = models.CharField(max_length=100)
    telefono_proveedor = models.CharField(max_length=100)
    ruc_proveedor = models.CharField(max_length=100)
    email_proveedor = models.CharField(max_length=100)
     
    def __str__(self):
        return 'Ruc: '+ self.ruc_proveedor + ' ' + self.nombre_proveedor


