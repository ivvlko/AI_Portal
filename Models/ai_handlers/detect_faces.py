import cv2
from PIL import Image
import cv2
from urllib.request import urlopen
import numpy as np


def detect_faces(pic, strength):
    req = urlopen(pic)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)
    strength = 1 + (1.51 - strength)
    image = cv2.resize(img, (500, 300), interpolation=cv2.INTER_AREA)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cascade_ai = cv2.CascadeClassifier('Models/ai_handlers/haarcascade_frontalface_default.xml')
    faces = cascade_ai.detectMultiScale(gray_image, strength, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray_image[y:y + h, x:x + w]
        roi_color = image[y:y + h, x:x + w]

    rgb = Image.fromarray(image)
    cv2.imwrite(f'static/processed/pic.jpg', image)
    return rgb