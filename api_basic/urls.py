from django.urls import path
from . import views

urlpatterns = [
    # path('articles/', views.article_list),
    path('articles/', views.ArticleAPIView.as_view()),
    # path('article_detail/<int:pk>/', views.article_detail),
    path('article_detail/<int:id>/', views.ArticleDetails.as_view()),
    # path('')
]