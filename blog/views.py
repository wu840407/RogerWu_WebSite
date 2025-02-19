# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm

def post_list(request):
    # 只取已發佈的文章，並依建立時間倒序排序
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, post_id):
    # 根據文章 ID 取得文章，若不存在則回傳 404 頁面
    post = get_object_or_404(Post, pk=post_id, published=True)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # 建立留言但暫不儲存到資料庫
            comment = form.save(commit=False)
            comment.post = post  # 連結到對應的文章
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'blog/detail.html', context)
