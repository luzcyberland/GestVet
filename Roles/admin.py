from django.contrib import admin
from .models import Rol

# Register your models here.
class RolesAdmin(admin.ModelAdmin):
    list_display = ('id_rol', 'nombre_rol','estado')
    list_display_links = ('nombre_rol',)

admin.site.register(Rol, RolesAdmin)