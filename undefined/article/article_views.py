from datetime import datetime

from article.models import Article
from article.serializer import ArticleSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions


class ArticleView(APIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['created_at'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        request.data['updated_at'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        print(request.data['updated_at'])
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
