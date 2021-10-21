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
    id_cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre_paciente 


class Vacunacion(models.Model):
    id_vacuna = models.AutoField(primary_key=True)
    fecha_vacunacion = models.DateField()
    vacuna_usada = models.CharField(max_length=50)
    tipo_vacuna = models.CharField(max_length=50)
    fecha_revacunacion = models.DateField()
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}'.format(self.id_vacuna)
    def save(self):
        super(Vacunacion, self).save()

class Historial(models.Model):
    id_historial = models.AutoField(primary_key=True)
    fecha_historial = models.DateField()
    descripcion_historial = models.CharField(max_length=255)
    id_paciente_historial = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.id_historial)
    def save(self):
        super(Historial, self).save()




    
