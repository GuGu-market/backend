from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.Serializer):
    category = serializers.CharField(max_length=30)
    product_name = serializers.CharField(max_length=15)
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()
    product_image = serializers.CharField(max_length=500)
    created_at = serializers.DateTimeField(input_formats=None)
    updated_at = serializers.DateTimeField(input_formats=None)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category = validated_data.get('category', instance.category)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance