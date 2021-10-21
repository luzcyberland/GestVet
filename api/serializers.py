from rest_framework import serializers
from Inventario.models import ProductoServicio
from Facturacion.models import Factura


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoServicio
        fields = '__all__'


class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'