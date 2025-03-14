from django.urls import path
from . import views
from .views import schedule_twitter_scraper

urlpatterns = [
    # 列表頁面：顯示所有文章
    path('', views.article_list, name='article_list'),
    # 詳細頁面：根據文章 ID 顯示單篇文章內容
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('schedule/', schedule_twitter_scraper, name='schedule_twitter'),
]
