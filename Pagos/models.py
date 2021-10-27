from django.db import models
from django.db.models.base import Model
from django.db.models.fields import AutoField
from Facturacion.models import Factura
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.

class Pagos(models.Model):
    id_pago = models.AutoField(primary_key=True)
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_pago = models.DateTimeField(auto_now_add=True)
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
        self.estado_pago = 'Pagado'
        '''factura_buscar = re.findall('[0-9]', str(self.factura))
        id_pago_factura = int(''.join(factura_buscar))

        fac = Factura.objects.filter(id_factura=id_pago_factura).values_list() #IVA del producto
        print(fac[9]'''
        super(Pagos, self).save()

@receiver(post_save, sender=Pagos)
def guardarEstadoFactura(sender, instance, **kwargs):
    idFactura = instance.factura.id_factura
    factura = Factura.objects.get(pk=idFactura)
    if factura:
        factura.estado_factura = 'Pagado'
        factura.save()



    

