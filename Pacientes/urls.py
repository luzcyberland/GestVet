from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import url, include
from Pacientes.views import PacientesListView, PacienteUpdate


urlpatterns=[
    url('agregar_paciente/',PacientesListView,name='crearpaciente'),
    path('listar_pacientes/', login_required(PacientesListView.as_view()), name='listarpacientes'),
    path('modificar_paciente/<pk>/',login_required(PacienteUpdate.as_view()), name='modificarpaciente'),
]