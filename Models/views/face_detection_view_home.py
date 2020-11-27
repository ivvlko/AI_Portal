from django.views.generic import TemplateView


class FaceDetection(TemplateView):
    template_name = 'models/face_detection_home.html'
