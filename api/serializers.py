from rest_framework import serializers
from Inventario.models import ProductoServicio
from Facturacion.models import Factura
from Compras.models import FacturaCompra, OrdenCompra


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoServicio
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenCompra
        fields = '__all__'

class FacturaCompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacturaCompra
        fields = '__all__'