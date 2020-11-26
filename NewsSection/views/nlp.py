from django.shortcuts import render
from NewsSection.models import News
from django.views.generic import ListView


class NLPView(ListView):
    template_name = 'news/nlp.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all().filter(category='Natural Language Processing').order_by('-date_posted')