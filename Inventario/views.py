from .forms import MarcaForm, ProductoServicioForm, UnidadMedidaForm
from django.shortcuts import render
from custom_decorators.decorators_2 import rol_required
from django.shortcuts import render, redirect
from Inventario.models import *
from django.views import generic
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator



######################################################################
#                 vistas para la unidad de medida                   #
#####################################################################
@rol_required('Recepcion')#Requiere Rol de Recepcion
def add_unidad_medida(request):
    form = ""
    if request.method == 'POST':
        form = UnidadMedidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar_unidad_medida/')
    else: 
        form=UnidadMedidaForm
    return render(request,'unidad_medida/agregar_unidad_medida.html',{'form':form})

@method_decorator(rol_required('Recepcion'), name='dispatch')
class UnidadMedidaView(generic.ListView):
    model = UnidadMedida
    context_object_name = 'unidad_medida_list' 
    template_name = 'unidad_medida/listar_unidad_medida.html'    
    def get_queryset(self):
        return UnidadMedida.objects.all()

@method_decorator(rol_required('Recepcion'), name='dispatch')
class UnidadMedidaUpdate(UpdateView):
    model = UnidadMedida
    fields =['id_unidad_medida','descripcion']
    template_name = 'unidad_medida/modificar_unidad_medida.html'
    success_url=reverse_lazy('listar_unidad_medida')
    
@rol_required('Recepcion')
def eliminar_unidad_medida(request, id_unidad_medida):
    req = UnidadMedida.objects.get(id_unidad_medida=id_unidad_medida)
    req.delete()
    return redirect('/listar_unidad_medida/')


######################################################################
#                 vistas para la marca                              #
#####################################################################
@rol_required('Recepcion')#Requiere Rol de Recepcion
def add_marca(request):
    form = ""
    if request.method == 'POST':
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar_marcas/')
    else: 
        form=MarcaForm
    return render(request,'marca/agregar_marca.html',{'form':form})

@method_decorator(rol_required('Recepcion'), name='dispatch')
class MarcaView(generic.ListView):
    model = Marca
    context_object_name = 'marca_list' 
    template_name = 'marca/listar_marcas.html'    
    def get_queryset(self):
        return Marca.objects.all()

@method_decorator(rol_required('Recepcion'), name='dispatch')
class MarcaUpdate(UpdateView):
    model = Marca
    fields =['id_marca','descripcion']
    template_name = 'marca/modificar_marca.html'
    success_url=reverse_lazy('listar_marcas')
    
@rol_required('Recepcion')
def eliminar_marca(request, id_marca):
    req = Marca.objects.get(id_marca=id_marca)
    req.delete()
    return redirect('/listar_marcas/')



######################################################################
#                 vistas para el producto o servicio                #
#####################################################################

@rol_required('Recepcion')#Requiere Rol de Recepcion
def add_pruducto_servicio(request):
    form = ""
    if request.method == 'POST':
        form = ProductoServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar_productos_servicios/')
    else: 
        form=ProductoServicioForm
    return render(request,'productos_servicios/agregar_producto_servicio.html',{'form':form})

@method_decorator(rol_required('Recepcion'), name='dispatch')
class ProductoServicioView(generic.ListView):
    model = ProductoServicio
    context_object_name = 'producto_servicio_list' 
    template_name = 'productos_servicios/listar_producto_servicio.html'    
    def get_queryset(self):
        return ProductoServicio.objects.all()

@method_decorator(rol_required('Recepcion'), name='dispatch')
class ProductoServicioUpdate(UpdateView):
    model = ProductoServicio
    fields =[
            'id_producto_servicio',
            'codigoBarra',
            'descripcion',
            'precio',
            'existencia',
            'ultimaCompra',
            'marca',
            'unidadMedida',
            'es_producto',
        ]
    template_name = 'productos_servicios/modificar_producto_servicio.html'
    success_url=reverse_lazy('listar_productos_servicios')
    
@rol_required('Recepcion')
def eliminar_producto_servicio(request, id_producto_servicio):
    req = ProductoServicio.objects.get(id_producto_servicio=id_producto_servicio)
    req.delete()
    return redirect('/listar_productos_servicios/')
