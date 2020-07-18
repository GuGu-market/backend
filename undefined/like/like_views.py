from datetime import datetime

from django.http import Http404
from django.forms.models import model_to_dict

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from like.models import Like
from like.serializer import LikeSerializer
from article.models import Article
from article.serializer import ArticleSerializer

class LikeView(APIView):
    def get(self, request, format=None):
        like = Like.objects.all()
        serializer = LikeSerializer(like, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        request.data['created_at'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        request.data['updated_at'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        like_serializer = LikeSerializer(data=request.data)

        if not like_serializer.is_valid():
            return Response(like_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        like_serializer.save()

        article_id = request.data.get('article_id')
        
        article_info = Article.objects.get(id=int(article_id))
        created_at = article_info.created_at

        updated_like_count_article =  model_to_dict(article_info)
        updated_like_count_article['created_at'] = created_at
        updated_like_count_article['updated_at'] = request.data['updated_at']

        article_serializer = ArticleSerializer(data=updated_like_count_article)
        
        if article_serializer.is_valid():
            article_serializer.like_count_update(article_info)
            return Response(article_serializer.data, status=status.HTTP_201_CREATED)
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, format=None):
        request.data['created_at'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        request.data['updated_at'] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        
        serializer = LikeSerializer(data=request.data)

        if serializer.is_valid():
            article_id = request.data.get('article_id')
            user_id = request.data.get('user_id')
            serializer.delete(article_id, user_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)