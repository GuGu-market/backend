from datetime import datetime

from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from product.models import Product
from product.serializer import ProductSerializer


class ProductView(APIView):
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['created_at'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        request.data['updated_at'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
