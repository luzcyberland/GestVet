from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from Pacientes.models import Paciente
from Pacientes.forms import PacienteForm
from django.views import generic
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.
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

class PacientesListView(generic.ListView):
    model = Paciente
    context_object_name = 'pacientes_list' 
    template_name = 'pacientes/listar_pacientes.html'

    def get_queryset(self):
        return Paciente.objects.all()

class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ['id_paciente', 'nombre_paciente', 'fecha_nacimiento', 'sexo_paciente', 'raza_paciente', 'especie_paciente','id_cliente']
    template_name = 'pacientes/modificar_paciente.html'
    success_url=reverse_lazy('listarpacientes')

def eliminar_paciente(request, id_paciente):
    req = Paciente.objects.get(id_paciente=id_paciente)
    req.delete()
    return redirect('/listar_pacientes/')
                  