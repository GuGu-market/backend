from datetime import datetime

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from auth.service import get_user_access_token

class AuthView(APIView):
    def get(self, request, format=None):
        return Response(get_user_access_token(request.data['access_token']))
