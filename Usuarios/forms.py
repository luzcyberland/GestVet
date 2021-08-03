from .models import Usuario
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'id_rol',
            'cedula',
            'telefono',
            'is_staff',
            'is_active',
            'is_superuser',
            'direccion'
        ]