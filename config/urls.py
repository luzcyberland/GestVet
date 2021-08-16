"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from django.urls import path
from Roles.views import add_rol, RolesListView, RolUpdate, eliminar_rol
from Usuarios.views import home, logoutUsuario
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', home, name='index'),
    path('logout/', logoutUsuario, name='logout'),
    path('crear_rol/', login_required(add_rol), name='crearrol'),
    path('listar_roles/', login_required(RolesListView.as_view()), name='listarroles'),
    path('modificar_rol/<pk>/',login_required(RolUpdate.as_view()), name='modificarrol'),
    path('eliminar_rol/<int:id_rol>/', login_required(eliminar_rol), name='eliminarrol'),

    
]
