from django.db.models.fields.mixins import FieldCacheMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.contrib.auth import authenticate
from datetime import datetime
from .models import FacturaCompra,DetalleFacturaCompra
from Inventario.models import ProductoServicio
import Inventario.views as inventario
from django.contrib import messages
from Proveedores.models import Proveedor
from custom_decorators.decorators_2 import rol_required
from django.utils.decorators import method_decorator
from Compras.models import FacturaCompra, DetalleFacturaCompra

# Create your views here.
@method_decorator(rol_required('Recepcion'), name='dispatch')
class listarFacturas(generic.ListView):
    model = FacturaCompra
    template_name = "compras/listarFacturas.html"
    context_object_name = "facturas"


@rol_required('Recepcion')
def nuevaFactura(request, id=None):
    template_name = 'compras/nuevaFactura.html'
    detalleFactura = {}
    proveedores = Proveedor.objects.filter()

    if request.method == "GET":
        factura = FacturaCompra.objects.filter(pk=id).first()

        if not factura:
            encabezado = {
                'id_factura_compra': 0,
                'fecha': datetime.today(),
                'fecha_factura': '',
                'proveedor': 0,
                'subTotal': 0.00,
                'descuento': 0.00,
                'total': 0.00,
                'monto_exento':0.00,
                'monto_iva':0.00,
                'monto_gravado':0.00
            }

            detalleFactura = None
        else:
            encabezado = {
                'id_factura_compra': factura.id_factura_compra,
                'fecha': factura.fecha,
                'fecha_factura': factura.fecha_factura,
                'proveedor': factura.proveedor,
                'subTotal': factura.subTotal,
                'descuento': factura.descuento,
                'total': factura.total,
                'monto_exento':factura.monto_exento,
                'monto_iva':factura.monto_iva,
                'monto_gravado':factura.monto_gravado
            }

        detalleFactura = DetalleFacturaCompra.objects.filter(factura_compra=factura)

        contexto = {
            "factura": encabezado,
            "detalleFactura": detalleFactura,
            "proveedores": proveedores
        }

        return render(request, template_name, contexto)

    if request.method == "POST":
        idProveedor = request.POST.get("proveedor")
        fecha = request.POST.get("fecha")
        fecha_factura = request.POST.get("fecha_factura")
        proveedor = Proveedor.objects.get(pk=idProveedor)

        if not id:
            factura = FacturaCompra(proveedor=proveedor, fecha=fecha, fecha_factura = fecha_factura)

            if factura:
                factura.save()

                id = factura.id_factura_compra
        else:
            factura = FacturaCompra.objects.filter(pk=id).first()

            if factura:
                factura.proveedor = proveedor

                factura.save()

        if not id:
            messages.error(request, 'No se puede detectar el Nr. de factura')
            
            return redirect("compras:listaFacturas")

        codigo = request.POST.get("codigo")
        cantidad = request.POST.get("cantidad")
        precio = request.POST.get("precio")
        subTotalDetalle = request.POST.get("subTotalDetalle")
        descuentoDetalle = request.POST.get("descuentoDetalle")
        totalDetalle = request.POST.get("totalDetalle")
        monto_gravado_det = request.POST.get("monto_gravado_det")
        monto_exento_det = request.POST.get("monto_exento_det")
        monto_iva_det = request.POST.get("monto_iva_det")
        if ProductoServicio.objects.filter(codigoBarra=codigo).exists():
            print('test-if')
            producto = ProductoServicio.objects.get(codigoBarra=codigo)
            detalleFactura = DetalleFacturaCompra(factura_compra=factura, producto=producto, cantidad=cantidad, precio=precio, subTotalDetalle=subTotalDetalle, descuentoDetalle=descuentoDetalle, totalDetalle=totalDetalle, monto_gravado_det= monto_gravado_det, monto_exento_det=monto_exento_det, monto_iva_det=monto_iva_det)
        else:
            messages.error(request, 'TEST')
        if detalleFactura:
            detalleFactura.save()
            
        return redirect("compras:editarFactura", id=id)

    return render(request, template_name, contexto)

@method_decorator(rol_required('Recepcion'), name='dispatch')
class verProductos(inventario.ProductoServicioView):
    template_name = "compras/buscarProducto.html"


def borrarDetalleFactura(request, id):
    template_name = "compras/borrarDetalleFactura.html"
    detalleFactura = DetalleFacturaCompra.objects.get(pk=id)

    if request.method == "GET":
        contexto = {"detalleFactura": detalleFactura}
    if request.method == "POST":
        detalleFactura.id = None
        detalleFactura.cantidad = (-1 * detalleFactura.cantidad)
        detalleFactura.subTotalDetalle = (-1 * detalleFactura.subTotalDetalle)
        detalleFactura.descuentoDetalle = (-1 * detalleFactura.descuentoDetalle)
        detalleFactura.totalDetalle = (-1 * detalleFactura.totalDetalle)
        detalleFactura.save()
        return HttpResponse("Ok")

        
    return render(request, template_name, contexto)
    


@rol_required('Recepcion')
def eliminar_factura(request, id_factura):
    if (id_factura != 0):
        req = FacturaCompra.objects.get(id_factura_compra=id_factura)
        req.delete()
        return redirect('compras:listarFacturas')
    else:
        return redirect('compras:listarFacturas')
    
