from django.views.generic import TemplateView


class SpamFilter(TemplateView):
    template_name = 'models/spam_filter_home.html'

