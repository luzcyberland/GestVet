from django import forms 
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Widget
from Clientes.models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        models = Cliente
        fields = (
            'id_cliente',
            'nombre_cliente',
            'apellido_cliente',
            'cedula_cliente',
            'direccion_cliente',
            'telefono_cliente',
            'ruc_cliente',
            'email_cliente',
        )
        
        labels = {
            'id_cliente' : 'ID Cliente',
            'nombre_cliente' : 'Nombre',
            'apellido_cliente' : 'Apellido',
            'cedula_cliente' : 'Cedula',
            'direccion_cliente' : 'Direccion',
            'telefono_cliente' : 'Telefono',
            'ruc_cliente' : 'RUC',
            'email_cliente' : 'Correo electronico'
        }
        
        widgets = {
            'id_cliente' : forms.NumberInput,
            'nombre_cliente' : forms.TextInput(attrs={'class':'form-control'}),
            'apellido_cliente' : forms.TextInput(attrs={'class':'form-control'}),
            'cedula_cliente' : forms.TextInput(attrs={'class':'form-control'}),
            'direccion_cliente' : forms.TextInput(attrs={'class':'form-control'}),
            'telefono_cliente' : forms.TextInput(attrs={'class':'form-control'}) ,
            'ruc_cliente' : forms.TextInput(attrs={'class':'form-control'}),
            'email_cliente' : forms.TextInput(attrs={'class':'form-control'}),
        }