from django.http import HttpResponse

def post_list(request):
    return HttpResponse("這是部落格文章列表頁面。")

def post_detail(request, post_id):
    return HttpResponse(f"這是部落格文章詳細頁面：文章 ID {post_id}")