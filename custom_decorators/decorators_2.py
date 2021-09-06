from django.contrib.auth.decorators import user_passes_test


def rol_required(id):
    """Verifica el rol del usuario antes de redireccionar"""
    def is_rol_required(usuario):
        if usuario.id_rol == id or usuario.is_superuser:
            return True
        else:
            return False            
    return user_passes_test(is_rol_required)
