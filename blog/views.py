# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    # 只取已發佈的文章，並依建立時間倒序排序
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, post_id):
    # 根據文章 ID 取得文章，若不存在則回傳 404 頁面
    post = get_object_or_404(Post, pk=post_id, published=True)
    return render(request, 'blog/detail.html', {'post': post})
