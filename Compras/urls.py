from django.urls import path
from Compras.views import  listarFacturas, verProductos,  nuevaFactura,  borrarDetalleFactura, eliminar_factura, listarOrdenes, nuevaOrden, borrarDetalleOrden, eliminar_orden
from django.contrib.auth.decorators import login_required


urlpatterns = [

    path('compras/', login_required(listarFacturas.as_view()), name="listarFacturas"),
    path('compras/buscarProducto', login_required(verProductos.as_view()), name="productosFactura"),
    path('compras/nuevaFactura', nuevaFactura, name="nuevaFactura"),
    path('compras/editarFactura/<int:id>', nuevaFactura, name="editarFactura"),
    path('compras/borrarDetalleFactura/<int:id>', borrarDetalleFactura, name="borrarDetalleFactura"),
    path('compras/eliminarFactura/<int:id_factura>/',login_required(eliminar_factura), name='eliminarFactura'),
    #orden
    path('compras/listarOrdenes', login_required(listarOrdenes.as_view()), name="listarOrdenes"),
    path('compras/nuevaOrden', nuevaOrden, name="nuevaOrden"),
    path('compras/editarOrden/<int:id>', nuevaOrden, name="editarOrden"),
    path('compras/borrarDetalleOrden/<int:id>', borrarDetalleOrden, name="borrarDetalleOrden"),
    path('compras/eliminarOrden/<int:id_orden>/',login_required(eliminar_orden), name='eliminarOrden'),

]
