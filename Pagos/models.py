'''from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField
from Facturacion.models import Factura
# Create your models here.

class Pagos(models.Model):
    id_pago = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField()
    monto_pago = models.FloatField(default=0)
    concepto_pago = models.CharField(max_length=200)
    PEN = 'Pendiente'
    PAG = 'Pagado'
    CAN = 'Cancelado'
    ESTADOS_PAGO = [(PEN, 'Pendiente'), (PAG, 'Pagado'), (CAN,'Cancelado')]
    estado_pago = models.CharField(max_length=20, choices=ESTADOS_PAGO, default=PEN)

    def __str__(self):
        return '{}'.format(self.id_pago)
    

    def save(self):
        
        self.monto_pago = self.subTotal - self.descuento

        super(Factura, self).save()'''
