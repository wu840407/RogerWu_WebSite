from django.shortcuts import render, get_object_or_404
from .models import Article
from .tasks import fetch_twitter_data
from django.http import HttpResponse

def article_list(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, 'knowledgebase/list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id, published=True)
    return render(request, 'knowledgebase/detail.html', {'article': article})

def schedule_twitter_scraper(request):
    # 這行會將任務加入排程，如果已加入則不會重複加入
    fetch_twitter_data(repeat=3600)  # 每3600秒重複
    return HttpResponse("已排程 Twitter 資料抓取任務。")
