# forum/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # 顯示所有版塊，可能已有 forum_index
    path('', views.forum_index, name='forum_index'),
    # 顯示特定版塊下的討論串列表
    path('forum/<int:forum_id>/', views.forum_threads, name='forum_threads'),
    # 發表新討論串（在特定版塊中）
    path('forum/<int:forum_id>/create/', views.create_thread, name='create_thread'),
    # 顯示討論串詳細內容與回覆
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
]

