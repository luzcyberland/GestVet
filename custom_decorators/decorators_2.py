from django.contrib.auth.decorators import user_passes_test


def rol_required(*args):
    """Verifica el rol del usuario antes de redireccionar"""
    
    
    def is_rol_required(usuario):
        lista_roles = [str(rol) for rol in args]
        if str(usuario.id_rol) in lista_roles or usuario.is_superuser:
            return True
            
    return user_passes_test(is_rol_required)
