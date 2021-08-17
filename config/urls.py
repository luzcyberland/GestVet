
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from Roles.views import add_rol, RolesListView, RolUpdate, eliminar_rol
from Usuarios.views import home,logoutUser

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('', home, name='index'),
    path('logout/', logoutUser, name='logout'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'), 
    path('crear_rol/', login_required(add_rol), name='crearrol'),
    path('listar_roles/', login_required(RolesListView.as_view()), name='listarroles'),
    path('modificar_rol/<pk>/',login_required(RolUpdate.as_view()), name='modificarrol'),
    path('eliminar_rol/<int:id_rol>/', login_required(eliminar_rol), name='eliminarrol'),   
]
#hello