from django.contrib import admin
from .models import Paciente, Vacunacion, Historial
# Register your models here.
class PacientesAdmin(admin.ModelAdmin):
    list_display = ('id_paciente', 'nombre_paciente', 'fecha_nacimiento', 'sexo_paciente', 'raza_paciente', 'especie_paciente')
    list_display_links = ('nombre_paciente',)

class VacunaAdmin(admin.ModelAdmin):
    list_display = (
            'id_vacuna',
            'fecha_vacunacion',
            'vacuna_usada',
            'tipo_vacuna',
            'fecha_revacunacion',
    )
    list_display_links = ('vacuna_usada',)

class HistorialAdmin(admin.ModelAdmin):
    list_display = (
            'id_historial',
            'fecha_historial',
            'descripcion_historial',
    )
    list_display_links = ('id_historial',)

admin.site.register(Paciente,PacientesAdmin)
admin.site.register(Vacunacion, VacunaAdmin)
admin.site.register(Historial, HistorialAdmin)