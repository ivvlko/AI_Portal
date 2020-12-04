from django.shortcuts import render

from NewsSection.forms import CommentForm
from NewsSection.models import News, Comment


def details_view(request, pk):
    current_news = News.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'current': current_news,
            'form': CommentForm(),
            'comments': Comment.objects.all().filter(news_id=pk).order_by('-date_posted')
        }
        return render(request, 'news/details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(name=request.user.username, comment=form.cleaned_data['comment'], news_id=pk)
            comment.save()
            context = {
                'current': current_news,
                'form': CommentForm(),
                'comments': Comment.objects.all().filter(news_id=pk).order_by('-date_posted')
            }
            return render(request, 'news/details.html', context)
        context = {
            'current': current_news,
            'form': CommentForm(request.POST),
            'comments': Comment.objects.all().filter(news_id=pk).order_by('-date_posted')
        }
        return render(request, 'news/details.html', context)

