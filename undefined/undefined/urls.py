from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from user import user_views
from article import article_views
from category import category_views
from like import like_views
from auth import auth_views
from point import point_views
from animal import animal_views


router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny),
)

urlpatterns = [
    url(r'^', include(router.urls)),
    url('admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('user/<int:user_id>/', user_views.UserView.as_view()),
    url('category/', category_views.CategoryView.as_view()),  
    url('article/', article_views.ArticleView.as_view()),
    url('like/', like_views.LikeView.as_view()),
    url('auth/', auth_views.AuthView.as_view()),
    url('point/', point_views.PointView.as_view()),
    url('animal/', animal_views.AnimalView.as_view()),

    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
]