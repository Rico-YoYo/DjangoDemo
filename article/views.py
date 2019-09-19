from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost


def article_list(request):
    # 取出所有文章
    articles = ArticlePost.objects.all()
    # 需要传递给模版的对象
    context = {'articles': articles}
    # render 函数，载入模版，并返回context对象
    return render(request, 'article/list.html', context)
