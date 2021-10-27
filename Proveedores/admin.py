from django.contrib import admin
from .models import Proveedor
# Register your models here.

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ( 'id_proveedor',
            'nombre_proveedor',
            'direccion_proveedor',
            'telefono_proveedor',
            'ruc_proveedor',
            'email_proveedor',)
    list_display_links = ('nombre_proveedor',)

admin.site.register(Proveedor,ProveedorAdmin)