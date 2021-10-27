from django.urls import path
from .views import  listarFacturas, verProductos,  nuevaFactura,  borrarDetalleFactura, eliminar_factura
from django.contrib.auth.decorators import login_required
from .reportes import imprimirFactura

urlpatterns = [

    path('facturas/', login_required(listarFacturas.as_view()), name="listarFacturas"),
    path('facturas/buscarProducto', login_required(verProductos.as_view()), name="productosFactura"),
    path('facturas/nuevaFactura', nuevaFactura, name="nuevaFactura"),
    path('facturas/editarFactura/<int:id>', nuevaFactura, name="editarFactura"),
    path('facturas/borrarDetalleFactura/<int:id>', borrarDetalleFactura, name="borrarDetalleFactura"),
    path('facturas/eliminarFactura/<int:id_factura>/',login_required(eliminar_factura), name='eliminarFactura'),
    path('facturas/imprimirFactura/<int:id>', imprimirFactura, name="imprimirFactura"),
]
