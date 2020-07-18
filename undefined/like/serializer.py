from rest_framework import serializers
from like.models import Like

class LikeSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    user_name = serializers.CharField(max_length=15, allow_blank=True)
    article_id = serializers.IntegerField()
    created_at = serializers.DateTimeField(input_formats=None)
    updated_at = serializers.DateTimeField(input_formats=None)

    class Meta:
        model = Like

    def create(self, validated_data):
        return Like.objects.create(**validated_data)

    def delete(self, article_id, user_id):
        like = Like.objects.filter(article_id=article_id, user_id=user_id) 
        
        if like:
            like.delete()