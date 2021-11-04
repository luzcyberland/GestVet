from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from Pacientes.models import Paciente, Vacunacion, Historial
from Pacientes.forms import PacienteForm, VacunaForm, HistorialForm
from django.views import generic
from django.views.generic import UpdateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from custom_decorators.decorators_2 import rol_required
from django.utils.decorators import method_decorator

######################################################################
#                 vistas para el paciente                            # 
#####################################################################

@rol_required('Recepcion','Doctor')
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


@method_decorator(rol_required('Recepcion','Doctor'), name='dispatch')
class PacientesListView(generic.ListView):
    model = Paciente
    context_object_name = 'pacientes_list' 
    template_name = 'pacientes/listar_pacientes.html'

    def get_queryset(self):
        return Paciente.objects.all()

@method_decorator(rol_required('Recepcion','Doctor'), name='dispatch')
class PacienteUpdate(UpdateView):
    model = Paciente
    fields = ['id_paciente', 'nombre_paciente', 'fecha_nacimiento', 'sexo_paciente', 'raza_paciente', 'especie_paciente','id_cliente']
    template_name = 'pacientes/modificar_paciente.html'
    success_url=reverse_lazy('listarpacientes')

@rol_required('Recepcion','Doctor')
def eliminar_paciente(request, id_paciente):
    req = Paciente.objects.get(id_paciente=id_paciente)
    req.delete()
    return redirect('/listar_pacientes/')

######################################################################
#                 vistas para la vacuna                              #
#####################################################################

@rol_required('Recepcion', 'Doctor')
def add_vacuna(request):
    form = ""
    if request.method == 'POST':
        form = VacunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar_vacunas/')
    else: 
        form=VacunaForm
    return render(request,'vacunas/crear_vacuna.html',{'form':form})

@method_decorator(rol_required('Recepcion','Doctor'), name='dispatch')
class VacunaUpdate(UpdateView):
    model = Vacunacion
    fields = ['id_vacuna',
            'fecha_vacunacion',
            'vacuna_usada',
            'tipo_vacuna',
            'fecha_revacunacion',
            'id_paciente']
    template_name = 'vacunas/modificar_vacuna.html'
    success_url=reverse_lazy('listar_vacunas')

@rol_required('Recepcion','Doctor')
def eliminar_vacuna(request, id_vacuna):
    req = Vacunacion.objects.get(id_vacuna=id_vacuna)
    req.delete()
    return redirect('/listar_vacunas/')     

@method_decorator(rol_required('Recepcion','Doctor'), name='dispatch')
class VacunasListView(generic.ListView):
    model = Vacunacion
    context_object_name = 'vacunas_list' 
    template_name = 'vacunas/listar_vacunas.html'

    def get_queryset(self):
        return Vacunacion.objects.all()        

@method_decorator(rol_required('Recepcion','Doctor'), name='dispatch')
class VacunasPacientesList(generic.ListView):
    model = Vacunacion
    context_object_name = 'vacunas_list' 
    template_name = 'vacunas/listar_vacunas_paciente.html'
    

    def get_queryset(self):
        self.vacuna = get_object_or_404(Paciente, id_paciente = self.kwargs['id_paciente'])
        return Vacunacion.objects.filter(id_paciente_id = self.kwargs['id_paciente'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente'] = Paciente.objects.get(id_paciente = self.kwargs['id_paciente'])
        return context 
######################################################################
#                 vistas para el historial                          # 
#####################################################################
@rol_required('Recepcion', 'Doctor')
def add_historial(request):
    form = ""
    if request.method == 'POST':
        form = HistorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listar_historial/')
    else: 
        form=HistorialForm
    return render(request,'historial/crear_historial.html',{'form':form})

@method_decorator(rol_required('Recepcion','Doctor'), name='dispatch')
class HistorialUpdate(UpdateView):
    model = Historial
    fields = ['id_historial',
            'fecha_historial',
            'descripcion_historial',
            'id_paciente_historial']
    template_name = 'historial/modificar_historial.html'
    success_url=reverse_lazy('listar_historial')

@rol_required('Recepcion', 'Doctor')
def eliminar_historial(request, id_historial):
    req = Historial.objects.get(id_historial=id_historial)
    req.delete()
    return redirect('/listar_historial/')

@method_decorator(rol_required('Recepcion','Doctor'), name='dispatch')
class HistorialListView(generic.ListView):
    model = Historial
    context_object_name = 'historial_list' 
    template_name = 'historial/listar_historial.html'

    def get_queryset(self):
        return Historial.objects.all()        

@method_decorator(rol_required('Recepcion','Doctor'), name='dispatch')
class HistorialPacientesList(generic.ListView):
    model = Historial
    context_object_name = 'historial_list' 
    template_name = 'historial/listar_historial_paciente.html'
    

    def get_queryset(self):
        self.historial = get_object_or_404(Paciente, id_paciente = self.kwargs['id_paciente'])
        return Historial.objects.filter(id_paciente_historial = self.kwargs['id_paciente'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente'] = Paciente.objects.get(id_paciente = self.kwargs['id_paciente'])
        return context 



    