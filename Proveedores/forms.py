from django import forms 
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Widget
from Proveedores.models import Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = (
            'id_proveedor',
            'nombre_proveedor',
            'direccion_proveedor',
            'telefono_proveedor',
            'ruc_proveedor',
            'email_proveedor',
        )