from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    email = serializers.CharField(max_length=30)
    username = serializers.CharField(max_length=15)
    image = serializers.CharField(max_length=500)
    grade = serializers.IntegerField()
    activate = serializers.BooleanField()
    phone = serializers.CharField(max_length=13)
    created_at = serializers.DateTimeField(format=None, input_formats=None, default_timezone=None)

    class Meta:
        model = User

    def create(self, validated_data):
        return Users.objects.create(**validated_data)
