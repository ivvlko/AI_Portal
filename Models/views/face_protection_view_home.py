from django.views.generic import TemplateView


class FaceProtection(TemplateView):
    template_name = 'models/face_protection_home.html'
