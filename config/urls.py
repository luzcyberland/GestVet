
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from Roles.views import add_rol, RolesListView, RolUpdate, eliminar_rol
from Usuarios.views import home, logoutUsuario, crear_usuario, UsuariosListView, UsuarioUpdate, eliminar_usuarios
from Clientes.views import add_cliente, ClientesListView, ClienteUpdate, eliminar_cliente
from Pacientes.views import add_paciente, PacienteUpdate, PacientesListView, eliminar_paciente, add_vacuna, VacunaUpdate, VacunasListView, eliminar_vacuna, VacunasPacientesList, HistorialListView, HistorialUpdate, add_historial, HistorialPacientesList, eliminar_historial

from Inventario.views import *

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
    path('eliminar_ciente/<int:id_cliente>/',login_required(eliminar_cliente), name='eliminarcliente'),
    path('crear_paciente/',login_required(add_paciente),name='crearpaciente'),
    path('listar_pacientes/',login_required(PacientesListView.as_view()), name = 'listarpacientes'),
    path('modificar_paciente/<pk>/',login_required(PacienteUpdate.as_view()),name='modificarpaciente'),
    path('eliminar_paciente/<int:id_paciente>',login_required(eliminar_paciente),name='eliminarpaciente'),
    path('agregar_marca/',login_required(add_marca),name='agregar_marca'),
    path('listar_marcas/', login_required(MarcaView.as_view()), name='listar_marcas'),
    path('modificar_marca/<pk>/',login_required(MarcaUpdate.as_view()), name='modificar_marca'),
    path('eliminar_marca/<int:id>/', login_required(eliminar_marca), name='eliminar_marca'),
    path('agregar_unidad_medida/',login_required(add_unidad_medida),name='agregar_unidad_medida'),
    path('listar_unidad_medida/', login_required(UnidadMedidaView.as_view()), name='listar_unidad_medida'),
    path('modificar_unidad_medida/<pk>/',login_required(UnidadMedidaUpdate.as_view()), name='modificar_unidad_medida'),
    path('eliminar_unidad_medida/<int:id>/', login_required(eliminar_unidad_medida), name='eliminar_unidad_medida'),
    path('agregar_producto_servicio/',login_required(add_pruducto_servicio),name='agregar_producto_servicio'),
    path('listar_productos_servicios/', login_required(ProductoServicioView.as_view()), name='listar_productos_servicios'),
    path('modificar_producto_servicio/<pk>/',login_required(ProductoServicioUpdate.as_view()), name='modificar_producto_servicio'),
    path('eliminar_producto_servicio/<int:id>/', login_required(eliminar_producto_servicio), name='eliminar_producto_servicio'),
    path('facturacion/', include(('Facturacion.urls', 'facturacion') ,namespace='facturacion')),
    path('api/', include(('api.urls', 'api'), namespace='api')),
    path('pagos/', include(('Pagos.urls', 'pagos') ,namespace='pagos')),
    path('crear_vacuna/',login_required(add_vacuna),name='crear_vacuna'),
    path('listar_vacunas/', login_required(VacunasListView.as_view()), name='listar_vacunas'),
    path('modificar_vacunas/<pk>/',login_required(VacunaUpdate.as_view()), name='modificar_vacuna'),
    path('eliminar_vacuna/<int:id_vacuna>',login_required(eliminar_vacuna),name='eliminar_vacuna'),
    path('listar_vacunas_paciente/<int:id_paciente>', login_required(VacunasPacientesList.as_view()), name='listar_vacunas_paciente'),
    path('listar_historial/', login_required(HistorialListView.as_view()), name='listar_historial'),
    path('modificar_historial/<pk>/',login_required(HistorialUpdate.as_view()), name='modificar_historial'),
    path('listar_historial_paciente/<id_paciente>', login_required(HistorialPacientesList.as_view()), name="listar_historial_paciente"),
    path('crear_historial/',login_required(add_historial),name='crear_historial'),
    path('eliminar_historial/<int:id_historial>',login_required(eliminar_historial),name='eliminar_historial'),
    ]
