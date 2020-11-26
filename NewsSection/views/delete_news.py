from django.shortcuts import render, redirect
from NewsSection.models import News


def delete_view(request, pk):
    current = News.objects.get(pk=pk)
    if request.method == 'GET':
        context = {'current': current}
        return render(request, 'news/delete.html', context)
    else:
        current.delete()
        return redirect('all_news_url')
