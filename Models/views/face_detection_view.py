from django.shortcuts import render
from Models.ai_handlers.detect_faces import detect_faces
from Models.forms import FaceDetectionForm
from django.contrib import messages
from Models.models import ProcessedPictureMixin
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
import random


def actual_face_detection_view(request):
    if request.method == 'GET':
        form = FaceDetectionForm()
        context = {'form': form}
        return render(request, 'models/actual_face_detection.html', context)
    else:
        form = FaceDetectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            actual = request.FILES['picture'].name
            response = f'https://django-ml-portal.s3.us-west-2.amazonaws.com/submitted_pictures/{actual}'
            strength = form.cleaned_data['strength']
            with NamedTemporaryFile(delete=True) as img_tmp:
                score = detect_faces(response, strength)
                score.save(img_tmp, format='JPEG')
                random_num = random.randint(1, 100000)
                img_tmp.flush()
                processed = ProcessedPictureMixin()
                processed.processed_picture.save(f'{actual}{random_num}.jpg', File(img_tmp))
                processed.save()
            context = {'form': form, 'score': f'https://django-ml-portal.s3.us-west-2.amazonaws.com/processed_pictures/{actual}{random_num}.jpg'}
            return render(request, 'models/actual_face_detection.html', context)
        messages.error(request, 'Please Upload Only JPG or PNG')
        return render(request, 'models/actual_face_detection.html', context={'form': FaceDetectionForm(request.POST)})

