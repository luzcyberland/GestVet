from django.contrib import admin
from .models import Paciente
# Register your models here.
class PacientesAdmin(admin.ModelAdmin):
    list_display = ('id_paciente', 'nombre_paciente', 'fecha_nacimiento', 'sexo_paciente', 'raza_paciente', 'especie_paciente')
    list_display_links = ('nombre_paciente',)

admin.site.register(Paciente,PacientesAdmin)