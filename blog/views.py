from django.shortcuts import render
from django.http import HttpResponse

from . models import Article

def home(request):

    #return HttpResponse("Hello world!")

    articles = Article.objects.all()

    context = {'articles': articles}

    return render(request, 'blog/index.html', context)


def singular_article(request, pk):

    article = Article.objects.get(id=pk)

    context = {'article': article}

    return render(request, 'blog/article.html', context)


    pass

