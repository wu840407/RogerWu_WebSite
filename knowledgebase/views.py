from django.shortcuts import render

# Create your views here.
def article_list(request):
    return HttpResponse("這是知識庫文章列表頁面。")

def article_detail(request, article_id):
    return HttpResponse(f"這是知識庫文章詳細頁面：文章 ID {article_id}")