from rest_framework import serializers
from Inventario.models import ProductoServicio


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoServicio
        fields = '__all__'
