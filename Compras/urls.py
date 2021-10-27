from django.urls import path
from Compras.views import  listarFacturas, verProductos,  nuevaFactura,  borrarDetalleFactura, eliminar_factura
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('compras/', login_required(listarFacturas.as_view()), name="listarFacturas"),
    path('compras/buscarProducto', login_required(verProductos.as_view()), name="productosFactura"),
    path('compras/nuevaFactura', nuevaFactura, name="nuevaFactura"),
    path('compras/editarFactura/<int:id>', nuevaFactura, name="editarFactura"),
    path('compras/borrarDetalleFactura/<int:id>', borrarDetalleFactura, name="borrarDetalleFactura"),
    path('compras/eliminarFactura/<int:id_factura>/',login_required(eliminar_factura), name='eliminarFactura'),

]
