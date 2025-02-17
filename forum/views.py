from django.http import HttpResponse

def forum_index(request):
    return HttpResponse("這是討論區首頁。")

def thread_detail(request, thread_id):
    return HttpResponse(f"這是討論串詳細頁面：討論串 ID {thread_id}")
