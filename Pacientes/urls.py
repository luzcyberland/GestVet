from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import url, include
from Pacientes.views import PacientesListView, PacienteUpdate, VacunasListView, VacunaUpdate, VacunasPacientesList, HistorialListView, HistorialUpdate, HistorialPacientesList
from .reportes import imprimirLibreta


urlpatterns=[
    url('agregar_paciente/',PacientesListView,name='crearpaciente'),
    path('listar_pacientes/', login_required(PacientesListView.as_view()), name='listarpacientes'),
    path('modificar_paciente/<pk>/',login_required(PacienteUpdate.as_view()), name='modificarpaciente'),
    url('crear_vacuna/',VacunasListView,name='crear_vacuna'),
    path('listar_vacunas/', login_required(VacunasListView.as_view()), name='listar_vacunas'),
    path('modificar_vacuna/<pk>/',login_required(VacunaUpdate.as_view()), name='modificar_vacuna'),
    path('listar_vacunas_paciente/<id_paciente>', login_required(VacunasPacientesList.as_view()), name='listar_vacunas_paciente'),
    path('listar_historial/', login_required(HistorialListView.as_view()), name='listar_historial'),
    path('modificar_historial/<pk>/',login_required(HistorialUpdate.as_view()), name='modificar_historial'),
    path('listar_historial_paciente/<id_paciente>', login_required(HistorialPacientesList.as_view()), name='listar_historial_paciente'),
    path('imprimirLibreta/<id>', imprimirLibreta, name="imprimirLibreta"),
]