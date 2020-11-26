from django.shortcuts import render
from NewsSection.models import News
from django.views.generic import ListView


class RoboticsView(ListView):
    template_name = 'news/robotics.html'
    context_object_name = 'news'
    ordering = ['-date_posted']

    def get_queryset(self):
        return News.objects.all().filter(category='Robotics').order_by('-date_posted')