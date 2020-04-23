from django.shortcuts import render

from .models import Article, Comment


# Create your views here.
def index(request):
    last_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'last_articles_list':last_articles_list})
