'''from django.contrib import admin
from .models import Pagos
# Register your models here.

class PagosAdmin(admin.ModelAdmin):
    list_display = ('id_pago','fecha_pago', 'monto_pago','concepto_pago','estado_pago')
    list_display_links = ('id_pago',)

admin.site.register(Pagos,PagosAdmin)'''
