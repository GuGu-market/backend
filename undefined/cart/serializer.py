from rest_framework import serializers
from cart.models import Cart

class CartSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    user_name = serializers.CharField(max_length=15)
    category = serializers.CharField(max_length=15)
    product_id = serializers.IntegerField()
    product_name = serializers.CharField(max_length=15)
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()
    product_image = serializers.CharField(max_length=500)
    created_at = serializers.DateTimeField(format="%Y-%m-%d",input_formats=['%Y-%m-%d',])
    updated_at = serializers.DateTimeField(format="%Y-%m-%d",input_formats=['%Y-%m-%d',])

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.category = validated_data.get('category', instance.category)
        instance.product_id = validated_data.get('product_id', instance.product_id)
        instance.product_name = validated_data.get('product_name', instance.product_name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.product_image = validated_data.get('product_image', instance.product_image)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance