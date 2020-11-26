<<<<<<< HEAD
=======
from django.shortcuts import render
>>>>>>> 10c795f36d23a00f8ab4fec4346b45eac822fd47
from NewsSection.models import News
from django.views.generic import ListView


class CvView(ListView):
    context_object_name = 'news'
    template_name = 'news/computer_vision.html'
<<<<<<< HEAD
    paginate_by = 2
=======
>>>>>>> 10c795f36d23a00f8ab4fec4346b45eac822fd47

    def get_queryset(self):
        return News.objects.all().filter(category='Computer Vision and Images').order_by('-date_posted')

