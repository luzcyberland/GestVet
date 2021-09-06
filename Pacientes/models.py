from django.db import models
from django.db.models.expressions import Exists
from Clientes.models import Cliente
# Create your models here.
class Paciente(models.Model):
    id_paciente = models.AutoField(primary_key=True)
    nombre_paciente = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    sexo_paciente = models.CharField(max_length=100)
    raza_paciente = models.CharField(max_length=100)
    especie_paciente = models.CharField(max_length=100)
    id_cliente = models.ForeignKey(Cliente,on_delete=models.DO_NOTHING, default=1)

    def __str__(self):
        return self.nombre_paciente
