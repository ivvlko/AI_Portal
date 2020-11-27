from skimage.feature import Cascade
from skimage.filters import gaussian
from skimage import data
import cv2


def find_all_faces(pic, strength):
    strength = 1 + (1.51 - strength)
    ml_model = data.lbp_frontal_face_cascade_filename()
    detector = Cascade(ml_model)
    faces = detector.detect_multi_scale(pic, scale_factor=strength, step_ratio=1, min_size=(10, 10), max_size=(500, 500))
    return faces


def cover_faces(faces, pic):

    def get_face(face):
        x, y = face['r'], face['c']
        width, height = face['width'] + face['r'], face['height'] + face['c']
        img_pic = pic[x: width, y: height]
        return img_pic

    def hide_face_with_gaussian(original, gaussian_face, face):
        x, y = face['r'], face['c']
        width, height = face['width'] + face['r'], face['height'] + face['c']
        pic[x:width, y:height] = gaussian_face
        return pic

    new_image = pic

    for face in faces:
        current_face = get_face(face)
        gaussian_img = gaussian(current_face, sigma=5, multichannel=True)
        new_image = hide_face_with_gaussian(faces, gaussian_img, face)

    if len(new_image) == 0:
        cv2.imwrite(f'static/processed/pic2.jpg', pic)
        return pic

    cv2.imwrite(f'static/processed/pic2.jpg', new_image)
    return new_image
