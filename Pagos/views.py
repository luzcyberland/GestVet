from django.shortcuts import render, redirect
from Pagos.models import Pagos
from Facturacion.models import Factura
from django.views import generic
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from custom_decorators.decorators_2 import rol_required
from django.utils.decorators import method_decorator
import Facturacion.views as facturacion
from datetime import datetime
from django.contrib import messages
# Create your views here.

@rol_required('Recepcion')
def nuevoPago(request, id=None):
    template_name = 'pagos/nuevoPago.html'
    facturas = Factura.objects.filter()

    if request.method == "GET":
        pago = Pagos.objects.filter(pk=id).first()

        if not pago:
            encabezado = {
                'id_pago': 0,
                'factura':0,
                'fecha_pago': datetime.today(),
                'monto_pago': 0.00,
                'concepto_pago' : ''
            }
        else:
            encabezado = {
                'id_pago': pago.id_pago,
                'factura': pago.factura,
                'fecha_pago': pago.fecha_pago,
                'monto_pago': pago.monto_pago,
                'concepto_pago' : pago.concepto_pago
            }

        contexto = {
            "pago": encabezado,
            "factura": facturas
        }

        return render(request, template_name, contexto)

    if request.method == "POST":
        idFactura = request.POST.get("codigo")
        fecha_pago = request.POST.get("fecha_pago")
        monto_pago = request.POST.get("precio")
        concepto_pago = request.POST.get("concepto_pago")
        factura = Factura.objects.get(pk=idFactura)

        if not id:
            pago = Pagos(factura=factura, fecha_pago=fecha_pago, monto_pago=monto_pago, concepto_pago = concepto_pago)

            if pago:
                pago.save()
                id = pago.id_pago
        else:
            pago = Pagos.objects.filter(pk=id).first()

            if pago:
                pago.factura = factura
                pago.save()

        if not id:
            messages.error(request, 'No se puede detectar el Nr. de pago')
            return redirect("pagos:listarPagos")

        return redirect("pagos:editarPago", id=id)

    return render(request, template_name, contexto)

@method_decorator(rol_required('Recepcion'), name='dispatch')
class PagosListView(generic.ListView):
    model = Pagos
    template_name = 'pagos/listarPagos.html'
    context_object_name = 'pagos'

    #def get_queryset(self):
        #return Pagos.objects.all()

@rol_required('Recepcion')
def eliminar_pago(request, id_pago):
    if (id_pago != 0):
        req = Pagos.objects.get(id_pago=id_pago)
        req.delete()
        return redirect('pagos:listarPagos')
    else:
        return redirect('pagos:listarPagos')

@method_decorator(rol_required('Recepcion'), name='dispatch')
class verFacturas(facturacion.listarFacturas):
    template_name = "pagos/buscarFactura.html"

