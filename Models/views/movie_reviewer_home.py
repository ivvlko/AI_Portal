from django.views.generic import TemplateView


class MovieReviewer(TemplateView):
    template_name = 'models/movie_reviewer_home.html'

