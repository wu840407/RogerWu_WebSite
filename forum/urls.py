from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum_index, name='forum_index'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
]