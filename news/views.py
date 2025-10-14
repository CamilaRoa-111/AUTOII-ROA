from django.shortcuts import render, get_object_or_404
from .models import Newss

def news(request):
    all_news = Newss.objects.all().order_by('-date')
    return render(request, 'news.html', {'news_list': all_news})

def news_detail(request, news_id):
    noticia = get_object_or_404(Newss, id=news_id)
    return render(request, 'news_detail.html', {'noticia': noticia})
