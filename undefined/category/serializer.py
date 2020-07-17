from rest_framework import serializers
from category.models import Category

class CategorySerializer(serializers.Serializer):
    category_name = serializers.CharField(max_length=15)
    category_image = serializers.CharField(max_length=500)
    created_at = serializers.DateTimeField(input_formats=None)
    updated_at = serializers.DateTimeField(input_formats=None)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name', instance.cartegory_name)
        instance.category_image = validated_data.get('category_image', instance.cartegory_image)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.updated_at = validated_data.get('updated_at', instance.updated_at)
        instance.save()
        return instance