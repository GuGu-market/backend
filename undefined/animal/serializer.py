from rest_framework import serializers
from animal.models import Animal

class AnimalSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    username = serializers.CharField(max_length=15, allow_blank=True)
    animal_id = serializers.IntegerField()
    image = serializers.CharField(max_length=500, allow_blank=True)
    created_at = serializers.DateTimeField(input_formats=None)

    class Meta:
        model = Animal

    def create(self, validated_data):
        return Animal.objects.create(**validated_data)
