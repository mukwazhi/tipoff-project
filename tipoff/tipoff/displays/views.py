# coding=utf-8
from django.shortcuts import render
from .models import Article, Brand


# Create your views here.
def article(request, slug):
    brand = Brand.objects.all()
    article_blog = Article.objects.get(slug=slug)
    context = {
        'brand': brand,
        'article_blog': article_blog
    }

    return render(request, 'article.html', context)
