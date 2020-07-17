from rest_framework import serializers
from article.models import Article

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(allow_null=True)
    user_id = serializers.IntegerField()
    user_name = serializers.CharField(max_length=15)
    title = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=500)
    like_count = serializers.IntegerField()
    created_at = serializers.DateTimeField(input_formats=None)
    updated_at = serializers.DateTimeField(input_formats=None)

    class Meta:
        model = Article

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        return Article.objects.update(**validated_data)

    def like_count_update(self, instance):
        print(Article.save(instance))