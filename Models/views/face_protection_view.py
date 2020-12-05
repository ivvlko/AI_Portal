from django.contrib import messages
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import render
from Models.ai_handlers.hide_faces import find_all_faces, cover_faces
from Models.forms import FaceProtectionForm
from urllib.request import urlopen
import numpy as np
import cv2
from PIL import Image
import random
from Models.models import ProcessedPictureMixin


def actual_face_protection_view(request):
    if request.method == 'GET':
        context = {'form': FaceProtectionForm()}
        return render(request, 'models/actual_face_protection.html', context)
    else:
        form = FaceProtectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            actual = request.FILES['picture'].name
            response = f'https://django-ml-portal.s3.us-west-2.amazonaws.com/submitted_pictures/{actual}'
            req = urlopen(response)
            arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
            img = cv2.imdecode(arr, -1)
            strength = form.cleaned_data['strength']
            all_faces = find_all_faces(img, strength)

            with NamedTemporaryFile(delete=True) as img_tmp:
                score = cover_faces(all_faces, img)
                score = Image.fromarray(score)
                score.save(img_tmp, format='JPEG')
                img_tmp.flush()
                processed = ProcessedPictureMixin()
                random_num = random.randint(1, 100000)
                processed.processed_picture.save(f'{actual}{random_num}.jpg', File(img_tmp))
                processed.save()
            context = {'form': form, 'score': f'https://django-ml-portal.s3.us-west-2.amazonaws.com/processed_pictures/{actual}{random_num}.jpg'}
            return render(request, 'models/actual_face_protection.html', context)
        messages.error(request, 'Please Upload Only JPG or PNG')
        return render(request, 'models/actual_face_protection.html', context={'form': FaceProtectionForm(request.POST)})
