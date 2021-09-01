from django.shortcuts import render, redirect
from Roles.models import Rol
from Roles.forms import RolForm
from django.views import generic
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

def add_rol(request):
    form = ""
    if request.method=='POST':
        form=RolForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar_roles/')
    else:
        form=RolForm ()
    
    return render(request, 'roles/crear_rol.html',{'form':form})

class RolesListView(generic.ListView):
    model = Rol
    context_object_name = 'roles_list' 
    template_name = 'roles/listar_roles.html'

    def get_queryset(self):
        return Rol.objects.all()

class RolUpdate(UpdateView):
    model = Rol
    fields = ['id_rol','nombre_rol','estado']
    template_name = 'roles/modificar_rol.html'
    success_url=reverse_lazy('listarroles')

def eliminar_rol(request, id_rol):
    req = Rol.objects.get(id_rol=id_rol)
    req.delete()
    return redirect('/listar_roles/')



