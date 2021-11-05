from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import ProductoSerializer, FacturaSerializer, FacturaCompraSerializer
from django.db.models import Q
from Inventario.models import ProductoServicio
from Facturacion.models import Factura
from Compras.models import FacturaCompra


class listarProductos(APIView):
    def get(self, request):
        producto = ProductoServicio.objects.all()
        datos = ProductoSerializer(producto, many=True).data

        return Response(datos)

class listarFacturas(APIView):
    def get(self, request):
        factura = Factura.objects.all()
        datos = FacturaSerializer(factura, many=True).data

        return Response(datos)

class detalleProducto(APIView):
    def get(self, request, codigo):
        producto = get_object_or_404(ProductoServicio, Q(codigo=codigo)|Q(codigoBarra=codigo))
        datos = ProductoSerializer(producto).data

        return Response(datos)

class listarFacturasCompras(APIView):
    def get(self, request):
        factura = FacturaCompra.objects.all()
        datos = FacturaCompraSerializer(factura, many=True).data
        return Response(datos)
