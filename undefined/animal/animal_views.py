from datetime import datetime

from django.http import Http404
from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from animal.models import Animal
from animal.serializer import AnimalSerializer
from point.models import Point
from point.serializer import PointSerializer

class AnimalView(APIView):
    def get(self, request, format=None):
        return Response()

    def post(self, request, format=None):
        request.data['created_at'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        ANIMAL_SAVE_POINT = 1

        point = Point.objects.get(user_id=request.data['user_id'])

        if point.point_amount < ANIMAL_SAVE_POINT:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        point_serializer = PointSerializer(point, {'point_amount': -ANIMAL_SAVE_POINT}, partial=True)
        
        if point_serializer.is_valid():
            point_serializer.save()
        
        animal_serializer = AnimalSerializer(data=request.data)

        if animal_serializer.is_valid():
            animal_serializer.save()
            return Response(animal_serializer.data, status=status.HTTP_400_BAD_REQUEST)

        return Response(animal_serializer.errors, status=status.HTTP_400_BAD_REQUEST)