from django.urls import path
from .views import listarProductos, detalleProducto, listarFacturas


urlpatterns = [
    path('productos/', listarProductos.as_view(), name="listaProductos"),
    path('pagos/', listarFacturas.as_view(), name="listaFacturas"),
    path('productos/<str:codigo>', detalleProducto.as_view(), name="detalleProducto")
]