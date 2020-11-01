from django.urls import path, include
from . import views
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('articles/', views.article_list),
    path('articles/', views.ArticleAPIView.as_view()),
    # path('article_detail/<int:pk>/', views.article_detail),
    path('article_detail/<int:id>/', views.ArticleDetails.as_view()),
    path('generic/articles/<int:id>/', views.GenericAPIView.as_view()),

]