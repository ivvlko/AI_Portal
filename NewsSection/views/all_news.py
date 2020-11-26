<<<<<<< HEAD
=======
from django.shortcuts import render
>>>>>>> 10c795f36d23a00f8ab4fec4346b45eac822fd47
from NewsSection.models import News
from django.views.generic import ListView


class AllNews(ListView):
    template_name = 'news/all_news.html'
    context_object_name = 'news'
<<<<<<< HEAD
    paginate_by = 2

    def get_queryset(self):
        return News.objects.all().order_by('-date_posted')


=======

    def get_queryset(self):
        return News.objects.all().order_by('-date_posted')
>>>>>>> 10c795f36d23a00f8ab4fec4346b45eac822fd47
