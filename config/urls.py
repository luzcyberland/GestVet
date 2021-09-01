
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from Roles.views import add_rol, RolesListView, RolUpdate, eliminar_rol
from Usuarios.views import home, logoutUsuario, crear_usuario, UsuariosListView, UsuarioUpdate, eliminar_usuarios
from Clientes.views import add_cliente, ClientesListView, ClienteUpdate, eliminar_cliente

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', home, name='index'),
    path('logout/', logoutUsuario, name='logout'),
    path('crear_rol/', login_required(add_rol), name='crearrol'),
    path('listar_roles/', login_required(RolesListView.as_view()), name='listarroles'),
    path('modificar_rol/<pk>/',login_required(RolUpdate.as_view()), name='modificarrol'),
    path('eliminar_rol/<int:id_rol>/', login_required(eliminar_rol), name='eliminarrol'),
    path('crear_usuario/',login_required(crear_usuario),name='crearusuario'),
    path('listar_usuarios/', login_required(UsuariosListView.as_view()), name='listarusuarios'),
    path('modificar_usuario/<pk>/',login_required(UsuarioUpdate.as_view()), name='modificarusuario'),
    path('eliminar_usuario/<int:id>/', login_required(eliminar_usuarios), name='eliminarusuario'),
    path('crear_cliente/',login_required(add_cliente),name='crearcliente'),
    path('listar_clientes/',login_required(ClientesListView.as_view()),name='listarclientes'),
    path('modificar_cliente/<pk>',login_required(ClienteUpdate.as_view()),name='modificarcliente'),
    path('eliminar_ciente/<int:id>',login_required(eliminar_cliente), name='eliminarcliente')
]
