from django import forms 
from django.forms import fields
from django.forms import widgets
from django.forms.widgets import Widget
from Inventario.models import *

class MarcaForm(forms.ModelForm):
    class Meta:
        model = Marca
        fields = ['id_marca', 'descripcion']
        labels = {'id_marca': 'ID Marca', 'descripcion': 'Descripcion'}
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UnidadMedidaForm(forms.ModelForm):
    class Meta:
        model = UnidadMedida
        fields = ['id_unidad_medida', 'descripcion']
        labels = {'id_unidad_medida': 'ID Unidad de Medida', 'descripcion': 'Descripcion' }
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class ProductoServicioForm(forms.ModelForm):
    class Meta:
        model = ProductoServicio
        fields = [
            'id_producto_servicio',
            'codigoBarra',
            'descripcion',
            'precio',
            'existencia',
            'ultimaCompra',
            'marca',
            'unidadMedida',
            'es_producto',
        ]
        
        labels = {
            'id_producto_servicio':'ID Producto/Servicio',
            'codigoBarra':'Codigo de Barra',
            'descripcion':'Descripción',
            'precio':'Precio',
            'existencia':'Existencia',
            'ultimaCompra':'Ultima Compra',
            'marca':'Marca',
            'unidadMedida':'Unidad de Medida',
            'es_producto':'Es Producto',
        }
        widget = {'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class': 'form-control'})