from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UserRegisterForm
from .models import Usuario
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import UpdateView
# Create your views here.

@login_required()
def home(request):
    return render(request,"base.html")

@login_required()
def logoutUsuario(request):
    logout(request)
    return redirect('/accounts/login/')

@login_required()
def crear_usuario(request):
    form=""
    if request.method=='POST':
        form=UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/listar_usuarios/')
    else:
        form=UserRegisterForm()
    
    return render(request, 'usuarios/crear_usuario.html',{'form':form})

class UsuariosListView(generic.ListView):
    model = Usuario
    context_object_name = 'usuarios_list' 
    template_name = 'usuarios/listar_usuarios.html'

    def get_queryset(self):
        return Usuario.objects.all()

class UsuarioUpdate(UpdateView):
    model = Usuario
    fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'id_rol',
            'cedula',
            'telefono',
            'is_staff',
            'is_active',
            'is_superuser',
            'direccion'
        ]
    template_name = 'usuarios/editar_usuario.html'
    success_url=reverse_lazy('listarusuarios')

def eliminar_usuarios(request, id):
    req = Usuario.objects.get(id=id)
    req.delete()
    return redirect('/listar_usuarios/')