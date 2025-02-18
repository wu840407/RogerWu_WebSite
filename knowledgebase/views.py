from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.filter(published=True).order_by('-created_at')
    return render(request, 'knowledgebase/list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id, published=True)
    return render(request, 'knowledgebase/detail.html', {'article': article})
