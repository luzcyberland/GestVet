from django.shortcuts import render

from .models import Vacunacion, Paciente, Historial


def imprimirLibreta(request, id):
    template_name = "pacientes/imprimirLibreta.html"
    vacunas = Vacunacion.objects.filter(id_paciente=id)
    paciente = Paciente.objects.filter(id_paciente= id)

    contexto = {
        'request': request,
        'vacunas': vacunas,
        'paciente':paciente
    }

    return render(request, template_name, contexto)