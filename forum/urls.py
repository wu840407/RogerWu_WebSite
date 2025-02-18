from django.urls import path
from . import views

urlpatterns = [
    # 討論區首頁：顯示所有版塊或討論串列表
    path('', views.forum_index, name='forum_index'),
    # 討論串詳細頁面：根據討論串 ID 顯示該討論串內容
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
]
