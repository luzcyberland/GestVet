from django.shortcuts import render

from .models import Vacunacion, Paciente, Historial


def imprimirLibreta(request, id):
    template_name = "pacientes/imprimirLibreta.html"
    vacunas = Vacunacion.objects.filter(id_paciente=id)
    paciente = Paciente.objects.filter(id_paciente= id)
    historiales= Historial.objects.filter(id_paciente_historial_id=id)

    contexto = {
        'request': request,
        'vacunas': vacunas,
        'paciente':paciente,
        'historiales':historiales
    }

    return render(request, template_name, contexto)

def imprimirHistorial(request, id):
    template_name = "pacientes/imprimirHistorial.html"
    paciente = Paciente.objects.filter(id_paciente= id)
    historiales= Historial.objects.filter(id_paciente_historial_id=id)

    contexto = {
        'request': request,
        'paciente':paciente,
        'historiales':historiales
    }

    return render(request, template_name, contexto)