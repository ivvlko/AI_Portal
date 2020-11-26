from django.shortcuts import render
from NewsSection.models import News


def details_view(request, pk):
    current_news = News.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'current': current_news,
        }
        return render(request, 'news/details.html', context)