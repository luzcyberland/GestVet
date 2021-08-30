from django.contrib import admin
from .models import Cliente
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre_cliente', 'apellido_cliente', 'cedula_cliente', 'direccion_cliente', 'telefono_cliente', 'ruc_cliente', 'email_cliente')
    list_display_links = ('nombre_cliente',)

admin.site.register(Cliente,ClientesAdmin)