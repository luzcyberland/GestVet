from django import forms 
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import NumberInput, Widget
from Pacientes.models import Paciente, Vacunacion, Historial

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = (
            'id_paciente',
            'nombre_paciente',
            'fecha_nacimiento',
            'sexo_paciente',
            'raza_paciente',
            'especie_paciente',
            'id_cliente'
        )
        
        labels = {
            'id_paciente' : 'Id del paciente',
            'nombre_paciente' : 'Nombre paciente',
            'fecha_nacimiento' : 'Fecha nacimiento',
            'sexo_paciente' : 'Sexo paciente',
            'raza_paciente' : 'Raza paciente',
            'especie_paciente' : 'Especie paciente',
            'id_cliente' : 'Dueño'
        }
        '''
        widgets = {
            'id_paciente' : forms.NumberInput,
            'nombre_paciente' : forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento' : forms.DateInput,
            'sexo_paciente' : forms.TextInput(attrs={'class':'form-control'}),
            'raza_paciente' : forms.TextInput(attrs={'class':'form-control'}),
            'especie_paciente' : forms.TextInput(attrs={'class':'form-control'}),
            'id_cliente' : forms.TextInput(attrs={'class':'form-control'})
        }
        '''
class VacunaForm(forms.ModelForm):
    class Meta:
        model = Vacunacion
        fields = (
            'id_vacuna',
            'fecha_vacunacion',
            'vacuna_usada',
            'tipo_vacuna',
            'fecha_revacunacion',
            'id_paciente'
        )

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = (
            'id_historial',
            'fecha_historial',
            'descripcion_historial',
            'id_paciente_historial'
        )


