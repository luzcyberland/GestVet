'''from django import forms
from django.db.models import fields
from .models import Pagos

class PagosForm(forms.ModelForm):
    class Meta:
        model = Pagos
        fields = (
            'id_pago',
            'factura',
            'fecha_pago', 
            'monto_pago',
            'concepto_pago',
            'estado_pago'
        )'''