from django.contrib import admin
from .models import Usuario

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('cedula','username', 'email', 'first_name', 'last_name', 'is_staff', 'telefono','direccion')

admin.site.register(Usuario, UserAdmin)