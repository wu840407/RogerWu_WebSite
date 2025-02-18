from django.shortcuts import render, get_object_or_404
from .models import Forum, Thread

def forum_index(request):
    forums = Forum.objects.all()
    return render(request, 'forum/index.html', {'forums': forums})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    return render(request, 'forum/thread.html', {'thread': thread})
