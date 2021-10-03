from django.contrib.auth.decorators import login_required
from django.urls import path
from django.conf.urls import url, include
from Inventario.views import *


urlpatterns=[
    url('agregar_producto_servicio/',ProductoServicioView,name='agregar_producto_servicio'),
    path('listar_productos_servicios/', login_required(ProductoServicioView.as_view()), name='listar_productos_servicios'),
    path('modificar_producto_servicio/<pk>/',login_required(ProductoServicioUpdate.as_view()), name='modificar_producto_servicio'),
    #unidad_medida
    url('agregar_unidad_medida/',UnidadMedidaView,name='agregar_unidad_medida'),
    path('listar_unidad_medida/', login_required(UnidadMedidaView.as_view()), name='listar_unidad_medida'),
    path('modificar_unidad_medida/<pk>/',login_required(UnidadMedidaUpdate.as_view()), name='modificar_unidad_medida'),
    #Marca
    url('agregar_marca/',MarcaView,name='agregar_marca'),
    path('listar_marcas/', login_required(MarcaView.as_view()), name='listar_marcas'),
    path('modificar_marca/<pk>/',login_required(MarcaUpdate.as_view()), name='modificar_marca')
]