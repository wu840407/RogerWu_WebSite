# forum/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Forum, Thread, Reply
from .forms import ThreadForm, ReplyForm

def forum_index(request):
    """
    顯示所有版塊的首頁
    """
    forums = Forum.objects.all()
    return render(request, 'forum/index.html', {'forums': forums})

def forum_threads(request, forum_id):
    """
    顯示特定版塊中的所有討論串
    """
    forum = get_object_or_404(Forum, pk=forum_id)
    threads = forum.threads.all().order_by('-created_at')
    return render(request, 'forum/threads.html', {'forum': forum, 'threads': threads})

@login_required
def create_thread(request, forum_id):
    """
    在特定版塊中發表新討論串
    只有登入的使用者才可發表
    """
    forum = get_object_or_404(Forum, pk=forum_id)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.forum = forum
            thread.creator = request.user
            thread.save()
            return redirect('thread_detail', thread_id=thread.id)
    else:
        form = ThreadForm()
    return render(request, 'forum/create_thread.html', {'form': form, 'forum': forum})

def thread_detail(request, thread_id):
    """
    顯示討論串的詳細內容與回覆，同時處理新回覆的提交
    """
    thread = get_object_or_404(Thread, pk=thread_id)
    replies = thread.replies.all().order_by('created_at')

    if request.method == 'POST':
        # 若使用者尚未登入，則導向登入頁面
        if not request.user.is_authenticated:
            return redirect('login')
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.thread = thread
            reply.author = request.user
            reply.save()
            return redirect('thread_detail', thread_id=thread.id)
    else:
        reply_form = ReplyForm()
    
    return render(request, 'forum/thread_detail.html', {
        'thread': thread,
        'replies': replies,
        'reply_form': reply_form,
    })
