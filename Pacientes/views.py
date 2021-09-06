from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from Pacientes.models import Paciente
from Pacientes.forms import PacienteForm
from django.views import generic
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from custom_decorators.decorators_2 import rol_required
from django.utils.decorators import method_decorator

# Create your views here.

@rol_required(2)
def add_paciente(request):
    form = ""
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar_pacientes/')
    else: 
        form=PacienteForm
    return render(request,'pacientes/crear_paciente.html',{'form':form})

@method_decorator(rol_required(2), name='dispatch')
class PacientesListView(generic.ListView):
    model = Paciente
    context_object_name = 'pacientes_list' 
    template_name = 'pacientes/listar_pacientes.html'

    def get_queryset(self):
        return Paciente.objects.all()

@method_decorator(rol_required(2), name='dispatch')
class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ['id_paciente', 'nombre_paciente', 'fecha_nacimiento', 'sexo_paciente', 'raza_paciente', 'especie_paciente','id_cliente']
    template_name = 'pacientes/modificar_paciente.html'
    success_url=reverse_lazy('listarpacientes')

@rol_required(2)
def eliminar_paciente(request, id_paciente):
    req = Paciente.objects.get(id_paciente=id_paciente)
    req.delete()
    return redirect('/listar_pacientes/')
                  