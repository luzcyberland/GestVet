'''from django.shortcuts import render, redirect
from Pagos.models import Pagos
from Pagos.forms import PagosForm
from django.views import generic
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from custom_decorators.decorators_2 import rol_required
from django.utils.decorators import method_decorator

# Create your views here.

@rol_required('Recepcion')
def agregar_pago(request):
    form = ""
    if request.method == 'POST':
        form = PagosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facturacion/listarFacturas.html')
    else: 
        form=PagosForm
    return render(request,'pagos/agregar_pago.html',{'form':form})

@method_decorator(rol_required('Recepcion'), name='dispatch')
class PagosListView(generic.ListView):
    model = Pagos
    context_object_name = 'pagos_list' 
    template_name = 'pagos/listar_pagos.html'

    def get_queryset(self):
        return Pagos.objects.all()

@method_decorator(rol_required('Recepcion'), name='dispatch')
class PagosUpdate(UpdateView):
    model = Pagos
    fields = ['id_pago',
            'factura',
            'fecha_pago', 
            'monto_pago',
            'concepto_pago',
            'estado_pago']
    template_name = 'pagos/modificar_pago.html'
    success_url=reverse_lazy('listarpagos')

@rol_required('Recepcion')
def eliminar_pago(request, id_pago):
    req = Pagos.objects.get(id_pago=id_pago)
    req.delete()
    return redirect('/listar_pagos/')'''

