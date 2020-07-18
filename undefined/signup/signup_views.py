from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request


from rest_framework import status

# from google.oauth2 import id_token
# from google.auth.transport import requests

from rest_framework.test import RequestsClient

# from users.models import Users
# from users.serialrizers import UsersSerializer


class GoogleLogin(APIView):
    def get(self, request, format=None):
        try:
            response = Request('https://www.django-rest-framework.org/api-guide/testing/')
            print(response)
        except ValueError as e:
            # Invalid token
            print(e)
            return Response(status=status.HTTP_201_CREATED)

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)