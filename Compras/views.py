from django.db.models.fields.mixins import FieldCacheMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.contrib.auth import authenticate
from datetime import datetime
from .models import FacturaCompra,DetalleFacturaCompra, OrdenCompra, DetalleOrdenCompra
from Inventario.models import ProductoServicio
import Inventario.views as inventario
from django.contrib import messages
from Proveedores.models import Proveedor
from custom_decorators.decorators_2 import rol_required
from django.utils.decorators import method_decorator
from Compras.models import FacturaCompra, DetalleFacturaCompra


@method_decorator(rol_required('Recepcion'), name='dispatch')
class listarOrdenes(generic.ListView):
    model = OrdenCompra
    template_name = "compras/listarOrdenes.html"
    context_object_name = "ordenes"

@rol_required('Recepcion')
def nuevaOrden(request, id=None):
    template_name = 'compras/nuevaOrden.html'
    detalleOrden = {}
    proveedores = Proveedor.objects.filter()

    if request.method == "GET":
        orden = OrdenCompra.objects.filter(pk=id).first()
        factura = FacturaCompra.objects.filter(pk=id).first()
        if not orden:
            encabezado = {
                'id_orden_compra': 0,
                'fecha': datetime.today(),
                'proveedor': 0,
                'subTotal': 0.00,
                'descuento': 0.00,
                'total': 0.00,
                'monto_exento':0.00,
                'monto_iva':0.00,
                'monto_gravado':0.00
            }

            detalleOrden = None
        else:
            encabezado = {
                'id_orden_compra': orden.id_orden_compra,
                'fecha': orden.fecha,
                'proveedor': orden.proveedor,
                'subTotal': orden.subTotal,
                'descuento': orden.descuento,
                'total': orden.total,
                'monto_exento': orden.monto_exento,
                'monto_iva': orden.monto_iva,
                'monto_gravado': orden.monto_gravado
            }

        detalleOrden = DetalleOrdenCompra.objects.filter(orden_compra=orden)

        contexto = {
            "orden": encabezado,
            "detalleOrden": detalleOrden,
            "proveedores": proveedores
        }

        return render(request, template_name, contexto)

    if request.method == "POST":
        idProveedor = request.POST.get("proveedor")
        fecha = request.POST.get("fecha")
        proveedor = Proveedor.objects.get(pk=idProveedor)

        if not id:
            orden = OrdenCompra(proveedor=proveedor, fecha=fecha)
            
            if orden:
                orden.save()
                id = orden.id_orden_compra
                factura = FacturaCompra(proveedor=proveedor, fecha=fecha, id_ref_compra = id)
                factura.save()

        else:
            orden = OrdenCompra.objects.filter(pk=id).first()
            factura = FacturaCompra.objects.filter(id_ref_compra=id).first() 
            if orden:
                orden.proveedor = proveedor
                factura.proveedor = proveedor 
                orden.save()
                factura.save()

        if not id:
            messages.error(request, 'No se puede detectar el Nr. de orden')
            
            return redirect("compras:listarOrdenes")

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
            detalleOrden = DetalleOrdenCompra(orden_compra=orden, producto=producto, cantidad=cantidad, precio=precio, subTotalDetalle=subTotalDetalle, descuentoDetalle=descuentoDetalle, totalDetalle=totalDetalle, monto_gravado_det= monto_gravado_det, 
            monto_exento_det=monto_exento_det, monto_iva_det=monto_iva_det)
            detalleFactura = DetalleFacturaCompra(factura_compra=factura, producto=producto, cantidad=cantidad, precio=precio, subTotalDetalle=subTotalDetalle, descuentoDetalle=descuentoDetalle, totalDetalle=totalDetalle, monto_gravado_det= monto_gravado_det, monto_exento_det=monto_exento_det, monto_iva_det=monto_iva_det)
        else:
            messages.error(request, 'TEST')
        if detalleOrden:
            detalleOrden.save()
            detalleFactura.save()
            
        return redirect("compras:editarOrden", id=id)
    return render(request, template_name, contexto)

@method_decorator(rol_required('Recepcion'), name='dispatch')
class verProductos(inventario.ProductoServicioView):
    template_name = "compras/buscarProducto.html"


def borrarDetalleOrden(request, id):
    template_name = "compras/borrarDetalleOrden.html"
    detalleOrden = DetalleOrdenCompra.objects.get(pk=id)

    if request.method == "GET":
        contexto = {"detalleOrden": detalleOrden}
    if request.method == "POST":
        detalleOrden.id = None
        detalleOrden.cantidad = (-1 * detalleOrden.cantidad)
        detalleOrden.subTotalDetalle = (-1 * detalleOrden.subTotalDetalle)
        detalleOrden.descuentoDetalle = (-1 * detalleOrden.descuentoDetalle)
        detalleOrden.totalDetalle = (-1 * detalleOrden.totalDetalle)
        detalleOrden.save()
        return HttpResponse("Ok")

        
    return render(request, template_name, contexto)
    


@rol_required('Recepcion')
def eliminar_orden(request, id_orden):
    if (id_orden != 0):
        req = OrdenCompra.objects.get(id_orden_compra=id_orden)
        req.delete()
        return redirect('compras:listarOrdenes')
    else:
        return redirect('compras:listarOrdenes')

######################################################################
#                        modelo para la factura                      #
#####################################################################
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
                'numero_factura': '',
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
                'numero_factura': factura.numero_factura,
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
        numero_factura = request.POST.get("numero_factura")
        proveedor = Proveedor.objects.get(pk=idProveedor)

        if not id:
            factura = FacturaCompra(proveedor=proveedor, fecha=fecha, fecha_factura = fecha_factura, numero_factura = numero_factura)

            if factura:
                factura.save()
                id = factura.id_factura_compra
        else:
            
            factura = FacturaCompra.objects.filter(pk=id).first()

            if factura:
                factura.proveedor = proveedor
                factura.numero_factura = numero_factura
                factura.fecha_factura = fecha_factura
                factura.save()

        if not id:
            messages.error(request, 'No se puede detectar el Nr. de factura')
            return redirect("compras:listaFacturas")
    return render(request, template_name)

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
    
