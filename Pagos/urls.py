from django.urls import path
from .views import PagosListView, nuevoPago, eliminar_pago, verFacturas, PagosListViewCompras, nuevoPagoCompras, eliminar_pagoCompras, verFacturasCompras
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('pagos/', login_required(PagosListView.as_view()), name="listarPagos"),
    path('pagos/buscarFactura', login_required(verFacturas.as_view()), name="pagosFactura"),
    path('pagos/nuevoPago', nuevoPago, name="nuevoPago"),
    path('pagos/editarPago/<int:id>', nuevoPago, name="editarPago"),
    path('pagos/eliminarPago/<int:id_pago>/',login_required(eliminar_pago), name='eliminarPago'),
    
    path('pagos/compras', login_required(PagosListViewCompras.as_view()), name="listarPagosCompras"),
    path('pagos/buscarFacturaCompras', login_required(verFacturasCompras.as_view()), name="pagosFacturaCompras"),
    path('pagos/nuevoPago/compras', nuevoPagoCompras, name="nuevoPagoCompras"),
    path('pagos/editarPago/compras/<int:id>', nuevoPagoCompras, name="editarPagoCompras"),
    path('pagos/eliminarPago/compras/<int:id_pago>/',login_required(eliminar_pagoCompras), name='eliminarPagoCompras'),
]
