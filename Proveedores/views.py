from custom_decorators.decorators_2 import rol_required
from django.shortcuts import render, redirect
from Proveedores.models import Proveedor
from Proveedores.forms import ProveedorForm
from django.views import generic
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
#from .decorators_2 import *


@rol_required('Recepcion')#Requiere Rol de Recepcion
def add_proveedor(request):
    form = ""
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar_proveedores/')
    else: 
        form=ProveedorForm
    return render(request,'proveedor/crear_proveedor.html',{'form':form})

@method_decorator(rol_required('Recepcion'), name='dispatch')
class ProveedoresListView(generic.ListView):
    model = Proveedor
    context_object_name = 'proveedores_list' 
    template_name = 'proveedor/listar_proveedores.html'    
    def get_queryset(self):
        return Proveedor.objects.all()

@method_decorator(rol_required('Recepcion'), name='dispatch')
class ProveedorUpdate(UpdateView):
    model = Proveedor
    fields = [ 'id_proveedor',
            'nombre_proveedor',
            'direccion_proveedor',
            'telefono_proveedor',
            'ruc_proveedor',
            'email_proveedor']
    template_name = 'proveedor/modificar_proveedor.html'
    success_url=reverse_lazy('listarproveedores')
    
@rol_required('Recepcion')
def eliminar_proveedor(request, id_proveedor):
    req = Proveedor.objects.get(id_proveedor=id_proveedor)
    req.delete()
    return redirect('/listar_proveedores/')
