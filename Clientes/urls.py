from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import url, include
from Clientes.views import ClientesListView, ClienteUpdate


urlpatterns=[
    url('agregar_cliente/',ClientesListView,name='crearcliente'),
    path('listar_cientes/', login_required(ClientesListView.as_view()), name='listarclientes'),
    path('modificar_cliente/<pk>/',login_required(ClienteUpdate.as_view()), name='modificarcliente'),
]