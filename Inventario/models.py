from django.db import models
from datetime import datetime

# Create your models here

class UnidadMedida(models.Model):
    id_unidad_medida = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500)

    def __str__(self):
        return self.descripcion

class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100, help_text='Descripción de la marca', unique=True)

    def __str__(self):
        return '{}'.format(self.descripcion)

    class Meta:
        verbose_name_plural = "Marcas"

class ProductoServicio (models.Model):
    id_producto_servicio =models.AutoField(primary_key=True)
    codigoBarra = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    existencia = models.FloatField(default=0)
    ultimaCompra = models.DateField(null=True, blank=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    unidadMedida = models.ForeignKey(UnidadMedida, on_delete=models.CASCADE)
    es_producto = models.BooleanField(default=True)
    #iva_5 = 5
    #iva_10 = 10
    #iva_exe = 0
    #porc_iva_op = [(iva_5, ('5')), (iva_10, ('10')), (iva_exe, ('0'))]
    #porc_iva = models.PositiveSmallIntegerField( choices= porc_iva_op, default= iva_exe)

    porc_iva = models.IntegerField(default=0)
    
    def __str__(self):
        return self.descripcion
