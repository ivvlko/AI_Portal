from django.shortcuts import render
<<<<<<< HEAD

from NewsSection.forms import CommentForm
from NewsSection.models import News, Comment
=======
from NewsSection.models import News
>>>>>>> 10c795f36d23a00f8ab4fec4346b45eac822fd47


def details_view(request, pk):
    current_news = News.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'current': current_news,
<<<<<<< HEAD
            'form': CommentForm(),
            'comments': Comment.objects.all().filter(news_id=pk).order_by('-date_posted')
        }
        return render(request, 'news/details.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(name=form.cleaned_data['name'], comment=form.cleaned_data['comment'], news_id=pk)
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
=======
        }
        return render(request, 'news/details.html', context)
>>>>>>> 10c795f36d23a00f8ab4fec4346b45eac822fd47
