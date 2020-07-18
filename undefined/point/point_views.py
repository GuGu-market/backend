from datetime import datetime

from point.models import Point
from point.serializer import PointSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class PointView(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        user_id = request.data['user_id']
        point = Point.objects.get(user_id=user_id)
        serializer = PointSerializer(point, many=True)
        return Response(serializer.data)

    def put(self, request, format=None):
        point = Point.objects.get(user_id=request.data['user_id'])
        serializer = PointSerializer(point, data={'point_amount': request.data['point_amount']}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        