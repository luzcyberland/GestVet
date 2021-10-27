from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from Proveedores.models import Proveedor
from Inventario.models import ProductoServicio

# Create your models here.
class FacturaCompra(models.Model):
    id_factura_compra = models.AutoField(primary_key=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_factura = models.DateTimeField()
    subTotal = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)
    monto_exento = models.FloatField(default=0)
    monto_iva = models.FloatField(default=0)
    monto_gravado= models.FloatField(default=0)
    PEN = 'Pendiente'
    PAG = 'Pagado'
    CAN = 'Cancelado'
    ESTADOS_FACTURA_COMPRA = [(PEN, 'Pendiente'), (PAG, 'Pagado'), (CAN,'Cancelado')]
    estado_factura_compra = models.CharField(max_length=20, choices=ESTADOS_FACTURA_COMPRA, default=PEN)

    def __str__(self):
        return '{}'.format(self.id_factura_compra)

    def save(self):
        
        self.total = self.subTotal - self.descuento

        super(FacturaCompra, self).save()

    class Meta:
        verbose_name_plural = "FacturasCompras"
        verbose_name = "FacturaCompra"
        

    
   

class DetalleFacturaCompra(models.Model):
    factura_compra = models.ForeignKey(FacturaCompra, on_delete=models.CASCADE)
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

        #print('PRODUCTO: ',pro[0][9])




        super(DetalleFacturaCompra, self).save()

    class Meta:
        verbose_name_plural = "Detalle facturas"
        verbose_name = "Detalle factura"


@receiver(post_save, sender=DetalleFacturaCompra)
def guardarDetalleFacturaCompra(sender, instance, **kwargs):
    idProducto = instance.producto.id_producto_servicio
    idFactura = instance.factura_compra.id_factura_compra
    factura = FacturaCompra.objects.get(pk=idFactura)
    if factura:
        subTotal = DetalleFacturaCompra.objects.filter(factura_compra=idFactura).aggregate(subTotal=Sum('subTotalDetalle')).get('subTotal', 0.00)
        descuento = DetalleFacturaCompra.objects.filter(factura_compra=idFactura).aggregate(descuento=Sum('descuentoDetalle')).get('descuento', 0.00)
        monto_exento = DetalleFacturaCompra.objects.filter(factura_compra=idFactura).aggregate(monto_exento=Sum('monto_exento_det')).get('monto_exento',0.00)
        monto_gravado = DetalleFacturaCompra.objects.filter(factura_compra=idFactura).aggregate(monto_gravado=Sum('monto_gravado_det')).get('monto_gravado',0.00)
        monto_iva = DetalleFacturaCompra.objects.filter(factura_compra=idFactura).aggregate(monto_iva=Sum('monto_iva_det')).get('monto_iva',0.00)

        factura.subTotal = subTotal
        factura.descuento = descuento
        factura.monto_exento = monto_exento
        factura.monto_gravado = monto_gravado
        factura.monto_iva = monto_iva

        factura.save()

    producto = ProductoServicio.objects.filter(pk=idProducto).first()

    if producto:
        cantidad = float(producto.existencia) + float(instance.cantidad)
        producto.existencia = cantidad
        producto.save()

