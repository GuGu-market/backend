from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    user_name = serializers.CharField(max_length=15)
    title = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=500)
    like_count = serializers.IntegerField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d",input_formats=['%Y-%m-%d',])
    updated_at = serializers.DateTimeField(format="%Y-%m-%d",input_formats=['%Y-%m-%d',])

    data = None

    def create(self, validated_data):
        return Article.objects.create(**validated_data)
