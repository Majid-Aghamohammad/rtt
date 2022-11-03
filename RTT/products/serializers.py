from rest_framework import serializers
from products.models import Product
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'product_id',
            'discussion',
            'price',
            'sold_number',
            'category',
            'quantity_counter',
            'available',
        ]



class InputProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'product_id',
            'discussion',
            'price',
            'sold_number',
            'category',
            'quantity_counter',
            'available',
            'created',
            'updated',
        ]

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = fields = '__all__'
