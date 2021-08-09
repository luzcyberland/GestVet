from django.contrib.auth.decorators import login_required
from django.urls import path
from GestVet.Roles.views import RolUpdate
from django.conf.urls import url, include
from Roles.views import RolesListView, RolUpdate


urlpatterns=[
    url('agregarRol/',RolesListView,name='crearrol'),
    path('listar_roles/', login_required(RolesListView.as_view()), name='listarroles'),
    path('modificarRol/<pk>/',login_required(RolUpdate.as_view()), name='modificarrol'),
    

]