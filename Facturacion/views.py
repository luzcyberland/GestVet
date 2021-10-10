from django.db.models.fields.mixins import FieldCacheMixin
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.contrib.auth import authenticate
from datetime import datetime
from .models import Cliente, Factura, DetalleFactura
from Inventario.models import ProductoServicio
import Inventario.views as inventario
from django.contrib import messages
from Clientes.models import Cliente
from custom_decorators.decorators_2 import rol_required
from django.utils.decorators import method_decorator
from Facturacion.models import Factura, DetalleFactura

# Create your views here.
@method_decorator(rol_required('Recepcion'), name='dispatch')
class listarFacturas(generic.ListView):
    model = Factura
    template_name = "facturacion/listarFacturas.html"
    context_object_name = "facturas"




@rol_required('Recepcion')
def nuevaFactura(request, id=None):
    template_name = 'facturacion/nuevaFactura.html'
    detalleFactura = {}
    clientes = Cliente.objects.filter()

    if request.method == "GET":
        factura = Factura.objects.filter(pk=id).first()

        if not factura:
            encabezado = {
                'id_factura': 0,
                'fecha': datetime.today(),
                'cliente': 0,
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
                'id_factura': factura.id_factura,
                'fecha': factura.fecha,
                'cliente': factura.cliente,
                'subTotal': factura.subTotal,
                'descuento': factura.descuento,
                'total': factura.total,
                'monto_exento':factura.monto_exento,
                'monto_iva':factura.monto_iva,
                'monto_gravado':factura.monto_gravado
            }

        detalleFactura = DetalleFactura.objects.filter(factura=factura)

        contexto = {
            "factura": encabezado,
            "detalleFactura": detalleFactura,
            "clientes": clientes
        }

        return render(request, template_name, contexto)

    if request.method == "POST":
        idCliente = request.POST.get("cliente")
        fecha = request.POST.get("fecha")
        cliente = Cliente.objects.get(pk=idCliente)

        if not id:
            factura = Factura(cliente=cliente, fecha=fecha)

            if factura:
                factura.save()

                id = factura.id_factura
        else:
            factura = Factura.objects.filter(pk=id).first()

            if factura:
                factura.cliente = cliente

                factura.save()

        if not id:
            messages.error(request, 'No se puede detectar el Nr. de factura')
            
            return redirect("facturacion:listaFacturas")

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
            detalleFactura = DetalleFactura(factura=factura, producto=producto, cantidad=cantidad, precio=precio, subTotalDetalle=subTotalDetalle, descuentoDetalle=descuentoDetalle, totalDetalle=totalDetalle, monto_gravado_det= monto_gravado_det, monto_exento_det=monto_exento_det, monto_iva_det=monto_iva_det)
        else:
            messages.error(request, 'TEST')
        if detalleFactura:
            detalleFactura.save()
            
        return redirect("facturacion:editarFactura", id=id)

    return render(request, template_name, contexto)

@method_decorator(rol_required('Recepcion'), name='dispatch')
class verProductos(inventario.ProductoServicioView):
    template_name = "facturacion/buscarProducto.html"


def borrarDetalleFactura(request, id):
    template_name = "facturacion/borrarDetalleFactura.html"
    detalleFactura = DetalleFactura.objects.get(pk=id)

    if request.method == "GET":
        contexto = {"detalleFactura": detalleFactura}
    if request.method == "POST":
        detalleFactura.id = None
        detalleFactura.cantidad = (-1 * detalleFactura.cantidad)
        detalleFactura.subTotalDetalle = (-1 * detalleFactura.subTotalDetalle)
        detalleFactura.descuentoDetalle = (-1 * detalleFactura.descuentoDetalle)
        detalleFactura.totalDetalle = (-1 * detalleFactura.totalDetalle)

        detalleFactura.save()
    
    return render(request, template_name, contexto)

    '''if request.method == "POST":
        user = request.POST.get("usuario")
        password = request.POST.get("password")
        usuario = authenticate(username=user, password=password)

        if not usuario:
            return HttpResponse("Usuario o contraseña incorrecta")

        if not usuario.is_active:
            return HttpResponse("Usuario inactivo")

        if usuario.is_superuser or usuario.has_perm("facturacion.sup_caja_detalleFactura"):
            detalleFactura.id = None
            detalleFactura.cantidad = (-1 * detalleFactura.cantidad)
            detalleFactura.subTotalDetalle = (-1 * detalleFactura.subTotalDetalle)
            detalleFactura.descuentoDetalle = (-1 * detalleFactura.descuentoDetalle)
            detalleFactura.totalDetalle = (-1 * detalleFactura.totalDetalle)

            detalleFactura.save()

            return HttpResponse("Ok")

        return HttpResponse("Usuario no autorizado")'''
