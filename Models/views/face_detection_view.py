from django.shortcuts import render
from Models.ai_handlers.detect_faces import detect_faces
from Models.forms import FaceDetectionForm
from django.contrib import messages


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
            response = f'https://ai-ml-portal.s3-us-west-2.amazonaws.com/submitted_pictures/{actual}'
            strength = form.cleaned_data['strength']
            score = detect_faces(response, strength)
            context = {'form': form, 'score': score}
            return render(request, 'models/actual_face_detection.html', context)
        messages.error(request, 'Please Upload Only JPG or PNG')
        return render(request, 'models/actual_face_detection.html', context={'form': FaceDetectionForm(request.POST)})
