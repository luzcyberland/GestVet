
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from Clientes.models import Cliente
from Inventario.models import ProductoServicio
from datetime import datetime, date
from django.forms import model_to_dict
import pytz


class Timbrado(models.Model):
    ACT='Activo'
    INA='Inactivo'
    ESTADO_TIMBRADO = [(ACT,'Activo'), (INA,'Inactivo')]
    id_timbrado = models.AutoField(primary_key=True)
    codigo_timbrado = models.CharField(max_length = 10, blank = False, verbose_name = 'Nro. Timbrado:')
    establecimiento = models.CharField(max_length=3, blank =True)
    punto_de_emision = models.CharField(max_length=3, blank =True)
    numero_inicio = models.IntegerField(default = 0, blank = False, verbose_name = 'Nro. Inicio:')
    numero_fin = models.IntegerField(default = 0, blank = False, verbose_name = 'Nro. Fin')
    numero_actual = models.IntegerField(default = 1, blank = False, verbose_name = 'Nro. Actual')
    fecha_vencimiento = models.DateField(blank = False,verbose_name ='Fecha de Vencimiento:')
    estado=models.CharField(max_length=10, choices=ESTADO_TIMBRADO, default=ACT)
    ruc = models.CharField(max_length = 10, default='0',verbose_name='Ruc')

    def clean(self):
        if self.fecha_vencimiento <= date.today():
            self.estado='Inactivo'
        else:
            if self.numero_inicio >= self.numero_actual:
                self.numero_actual = self.numero_inicio
            else:
                pass


    def __str__(self):
        return '{}'.format(self.codigo_timbrado)

######################################################################
#                        modelo para la factura                      #
#####################################################################

class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    timbrado = models.ForeignKey(Timbrado, on_delete=models.CASCADE, null = True, blank =True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nro_factura = models.CharField(max_length = 14, null=True, blank = True)
    fecha = models.DateField(auto_now_add=True)
    subTotal = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    monto_exento = models.FloatField(default=0)
    monto_iva = models.FloatField(default=0)
    monto_gravado= models.FloatField(default=0)
    PEN = 'Pendiente'
    PAG = 'Pagado'
    CAN = 'Cancelado'
    ESTADOS_FACTURA = [(PEN, 'Pendiente'), (PAG, 'Pagado'), (CAN,'Cancelado')]
    estado_factura = models.CharField(max_length=20, choices=ESTADOS_FACTURA, default=PEN)
    ruc = models.CharField(max_length = 10, default='0',verbose_name='Ruc')

    def __str__(self):
        return '{}'.format(self.id_factura)
    
    def toJSON(self):
        item = model_to_dict(self)
        item['cliente'] = self.cliente.toJSON()
        item['subTotal'] = format(self.subTotal, '.2f')
        item['monto_iva'] = format(self.monto_iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['fecha'] = self.fecha.strftime(r'%Y-%m-%d')
        #item['det'] = [i.toJSON() for i in self.detallefactura_set.all()]
        return item

    def save(self):
        
        self.total = self.subTotal - self.descuento

        super(Factura, self).save()
    

    class Meta:
        verbose_name_plural = "Facturas"
        verbose_name = "Factura"
        

    
   

class DetalleFactura(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    producto = models.ForeignKey(ProductoServicio, on_delete=models.CASCADE)
    cantidad = models.FloatField(default=0.0)
    precio = models.FloatField(default=0)
    subTotalDetalle = models.FloatField(default=0)
    descuentoDetalle = models.FloatField(default=0)
    totalDetalle = models.FloatField(default=0)
    monto_exento_det = models.FloatField(default=0)
    monto_iva_det = models.FloatField(default=0)
    monto_gravado_det= models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self):

        self.subTotalDetalle = float(float(self.cantidad)) * float(self.precio)
        self.totalDetalle = float(self.subTotalDetalle) - float(self.descuentoDetalle)

        pro = ProductoServicio.objects.filter(descripcion=self.producto).values_list() #IVA del producto


        if int(pro[0][9]) == 5:

            self.monto_exento_det = 0
            self.monto_gravado_det = self.subTotalDetalle
            self.monto_iva_det = 0

        elif int(pro[0][9]) == 10:
            self.monto_exento_det = 0
            self.monto_gravado_det = 0
            self.monto_iva_det = self.subTotalDetalle
        else:
            self.monto_exento_det = self.subTotalDetalle
            self.monto_gravado_det = 0
            self.monto_iva_det = 0

        print('PRODUCTO: ',pro[0][9])




        super(DetalleFactura, self).save()

    class Meta:
        verbose_name_plural = "Detalle facturas"
        verbose_name = "Detalle factura"


@receiver(post_save, sender=DetalleFactura)
def guardarDetalleFactura(sender, instance, **kwargs):
    idProducto = instance.producto.id_producto_servicio
    idFactura = instance.factura.id_factura
    factura = Factura.objects.get(pk=idFactura)
    if factura:
        subTotal = DetalleFactura.objects.filter(factura=idFactura).aggregate(subTotal=Sum('subTotalDetalle')).get('subTotal', 0.00)
        descuento = DetalleFactura.objects.filter(factura=idFactura).aggregate(descuento=Sum('descuentoDetalle')).get('descuento', 0.00)
        monto_exento = DetalleFactura.objects.filter(factura=idFactura).aggregate(monto_exento=Sum('monto_exento_det')).get('monto_exento',0.00)
        monto_gravado = DetalleFactura.objects.filter(factura=idFactura).aggregate(monto_gravado=Sum('monto_gravado_det')).get('monto_gravado',0.00)
        monto_iva = DetalleFactura.objects.filter(factura=idFactura).aggregate(monto_iva=Sum('monto_iva_det')).get('monto_iva',0.00)

        factura.subTotal = subTotal
        factura.descuento = descuento
        factura.monto_exento = monto_exento
        factura.monto_gravado = monto_gravado
        factura.monto_iva = monto_iva

        factura.save()

    producto = ProductoServicio.objects.filter(pk=idProducto).first()

    if producto:
        cantidad = float(producto.existencia) - float(instance.cantidad)
        producto.existencia = cantidad
        producto.save()

@receiver(post_save, sender=Factura)
def nro_fac_get(sender,instance,**kwargs):
    factura_id = instance.id_factura

    tim = Timbrado.objects.get(estado = 'Activo')
        
    factura = Factura.objects.get(pk=factura_id)

    if factura.nro_factura == None:
        if tim:
            if tim.numero_actual+1 <= tim.numero_fin:
                factura.timbrado = tim
                factura.ruc = tim.ruc
                factura.nro_factura=tim.establecimiento+'-'+tim.punto_de_emision+'-'+str(tim.numero_actual).zfill(6)
                tim.numero_actual = tim.numero_actual+1
                tim.save()
                factura.save()
            


