from django.contrib import messages
from django.shortcuts import render, redirect
from NewsSection.forms import NewsForm
from NewsSection.models import News


def update_view(request, pk):
    current_news = News.objects.get(pk=pk)
    if request.method == 'GET':
        form = NewsForm(instance=current_news)
        context = {'form': form, 'current': current_news}
        return render(request, 'news/update.html', context)
    else:
        form = NewsForm(request.POST, instance=current_news)
        if form.is_valid():
            form.author = News.author
            form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('all_news_url')
        context = {'form': form, 'current': current_news}
        return render(request, 'news/update.html', context)
