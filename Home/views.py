from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.base import TemplateView

from NewsSection.models import News


class HomePageView(TemplateView):
    template_name = 'home/home.html'


class AboutPageView(TemplateView):
    template_name = 'home/about.html'


class SearchResults(ListView):
    model = News
    template_name = 'home/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if len(query) > 0:
            object_list = News.objects.filter(
                Q(title__icontains=query) | Q(text__icontains=query)
            )
            return object_list
