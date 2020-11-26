from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from NewsSection.forms import NewsForm


@login_required()
def add_news_view(request):
    if request.method == 'GET':
        form = NewsForm()
        context = {'form': form}
        return render(request, 'news/add_news.html', context)
    else:
        form = NewsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author_id = request.user.id
            obj.save()
            return redirect('all_news_url')
        form = NewsForm(request.POST)
        context = {'form':form}
        return render(request, 'news/add_news.html', context)