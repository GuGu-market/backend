from rest_framework import serializers
from signup.models import Signup


class SignupSerializer(serializers.Serializer):
    def create(self, validated_data):
        return Signup.objects.create(**validated_data)