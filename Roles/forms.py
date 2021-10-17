from django import forms
from django.forms import fields
from django.forms.widgets import Widget 
from Roles.models import Rol

class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = (
            'id_rol',
            'nombre_rol',
            #'estado'
        )

        #labels = {
         #   'id_rol': 'ID Rol',
          #  'nombre_rol':'Nombre Rol',
            #'estado':'Estado'
        #}
        #widgets={
        #    'id_rol' : forms.NumberInput,
        #    'Nombre_rol': forms.TextInput(attrs={'class':'form-control'}),
            #'Estado': forms.TextInput(attrs={'class':'form-control'}),
        # }