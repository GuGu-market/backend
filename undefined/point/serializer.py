from rest_framework import serializers
from point.models import Point

class PointSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    user_id = serializers.IntegerField()
    username = serializers.CharField(max_length=15, allow_blank=True)
    point_amount = serializers.IntegerField()
    created_at = serializers.DateTimeField(input_formats=None)
    updated_at = serializers.DateTimeField(input_formats=None)

    class Meta:
        model = Point

    def create(self, validated_data):
        return Point.objects.create(**validated_data)

    def update(self, point_model, data):
        point_model.point_amount += data['point_amount']
        point_model.save()
        return point_model