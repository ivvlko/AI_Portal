from django.contrib import messages
from django.shortcuts import render
from Models.ai_handlers.hide_faces import find_all_faces, cover_faces
from Models.forms import FaceProtectionForm
from urllib.request import urlopen
import numpy as np
import cv2


def actual_face_protection_view(request):
    if request.method == 'GET':
        context = {'form': FaceProtectionForm()}
        return render(request, 'models/actual_face_protection.html', context)
    else:
        form = FaceProtectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            actual = request.FILES['picture'].name
            response = f'https://ai-ml-portal.s3-us-west-2.amazonaws.com/submitted_pictures/{actual}'
            req = urlopen(response)
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1)
            strength = form.cleaned_data['strength']
            all_faces = find_all_faces(img, strength)
            score = cover_faces(all_faces, img)
            context = {'form': form, 'score': score}
            return render(request, 'models/actual_face_protection.html', context)
        messages.error(request, 'Please Upload Only JPG or PNG')
        return render(request, 'models/actual_face_protection.html', context={'form': FaceProtectionForm(request.POST)})