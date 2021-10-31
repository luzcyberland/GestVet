from django import forms 
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import NumberInput, Widget
from Facturacion.models import Timbrado
from django.forms import ModelForm, DateInput

class TimbradoForm(forms.ModelForm):
    class Meta:
        model = Timbrado
        fields = (
            'id_timbrado',
            'codigo_timbrado', 
            'establecimiento',
            'punto_de_emision',
            'numero_inicio',
            'numero_fin',
            'numero_actual',
            'fecha_vencimiento',
            'estado',
            'ruc',
        )