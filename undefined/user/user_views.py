import json

from datetime import datetime

from django.http import Http404
from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

from animal.models import Animal
from animal.serializer import AnimalSerializer
from point.models import Point
from point.serializer import PointSerializer
from user.models import User
from user.serializer import UserSerializer

class UserView(APIView):
    def get(self, request, user_id, format=None):
        user = User.objects.get(id=user_id)
        user_serializer = UserSerializer(user)

        animals = Animal.objects.all().filter(user_id=user_id).values('animal_id', 'image')
        tmp_animals = []

        for animal in animals:
            tmp_animals.append(animal)

        try:
            point = Point.objects.get(user_id=user_id)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
        point_serializer = PointSerializer(point)
        result = {
            'user': user_serializer.data
        }

        result['user']['point'] = point_serializer.data
        result['user']['animal'] = json.loads(json.dumps(tmp_animals))

        return Response(result, status=status.HTTP_201_CREATED)
