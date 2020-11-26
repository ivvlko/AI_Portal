from django.shortcuts import render
from NewsSection.models import News
from django.views.generic import ListView


class AllNews(ListView):
    template_name = 'news/all_news.html'
    context_object_name = 'news'
    paginate_by = 2

    def get_queryset(self):
        return News.objects.all().order_by('-date_posted')



