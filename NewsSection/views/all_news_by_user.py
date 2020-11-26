from django.shortcuts import render
from NewsSection.models import News


def all_news_by_user_view(request):
    current = request.user
    news = News.objects.filter(author=current).order_by('-date_posted')

    if request.method == 'GET':
        context = {
            'news': news,
            'current': current,
        }
        return render(request, 'news/all_news_by_user.html', context)

