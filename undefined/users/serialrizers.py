from rest_framework import serializers
from users.models import Users


class UsersSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=30)
    user_name = serializers.CharField(max_length=15)
    password = serializers.CharField(max_length=30)
    grade = serializers.IntegerField()
    activate = serializers.BooleanField()
    phone = serializers.CharField(max_length=13)
    created_at = serializers.DateTimeField(format=None, input_formats=None, default_timezone=None)

    def create(self, validated_data):
        return Users.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.user_name = validated_data.get('user_name', instance.user_name)
        instance.password = validated_data.get('password', instance.password)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.activate = validated_data.get('activate', instance.activate)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.created_at = validated_data.get('created_at', instance.created_at)
        instance.save()
        return instance