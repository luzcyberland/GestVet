
from custom_decorators.decorators_2 import rol_required
from django.shortcuts import render, redirect
from Clientes.models import Cliente
from Clientes.forms import ClienteForm
from django.views import generic
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
#from .decorators_2 import *


@rol_required('Recepcion')#Requiere Rol de Recepcion
def add_cliente(request):
    form = ""
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar_clientes/')
    else: 
        form=ClienteForm
    return render(request,'clientes/crear_cliente.html',{'form':form})

@method_decorator(rol_required('Recepcion'), name='dispatch')
class ClientesListView(generic.ListView):
    model = Cliente
    context_object_name = 'clientes_list' 
    template_name = 'clientes/listar_clientes.html'    
    def get_queryset(self):
        return Cliente.objects.all()

@method_decorator(rol_required('Recepcion'), name='dispatch')
class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['id_cliente', 'nombre_cliente', 'apellido_cliente', 'cedula_cliente', 'direccion_cliente', 'telefono_cliente', 'ruc_cliente', 'email_cliente']
    template_name = 'clientes/modificar_cliente.html'
    success_url=reverse_lazy('listarclientes')
    
@rol_required('Recepcion')
def eliminar_cliente(request, id_cliente):
    req = Cliente.objects.get(id_cliente=id_cliente)
    req.delete()
    return redirect('/listar_clientes/')
                  