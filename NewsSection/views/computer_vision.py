from NewsSection.models import News
from django.views.generic import ListView


class CvView(ListView):
    context_object_name = 'news'
    template_name = 'news/computer_vision.html'
    paginate_by = 2

    def get_queryset(self):
        return News.objects.all().filter(category='Computer Vision and Images').order_by('-date_posted')

