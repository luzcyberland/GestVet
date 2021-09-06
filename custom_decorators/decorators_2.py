from django.contrib.auth.decorators import user_passes_test


def rol_required(id):
    """Verifica el rol del usuario antes de redireccionar"""
    
    
    def is_rol_required(usuario):
        
        if str(usuario.id_rol) == str(id) or usuario.is_superuser:
            return True
            
    return user_passes_test(is_rol_required)
