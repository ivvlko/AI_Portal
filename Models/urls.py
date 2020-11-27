from django.urls import path
from Models.views.face_detection_view import actual_face_detection_view
from Models.views.face_detection_view_home import FaceDetection
from Models.views.face_protection_view import actual_face_protection_view
from Models.views.face_protection_view_home import FaceProtection
from Models.views.models_home import models_home
from Models.views.movie_reviewer import actual_movie_reviewer_view
from Models.views.movie_reviewer_home import MovieReviewer
from Models.views.spam_filter_view import actual_spam_filter_view
from Models.views.spam_filter_view_home import SpamFilter
from Models.views.user_models import user_models_view

urlpatterns = [

    path('', models_home, name='models_home_url'),
    path('face_detection/', FaceDetection.as_view(), name='face_detection_url'),
    path('face_detection/test/', actual_face_detection_view, name='actual_face_detection_url'),
    path('spam_filter/', SpamFilter.as_view(), name='spam_filter_url'),
    path('spam_filter/test/', actual_spam_filter_view, name='actual_spam_filter_url'),
    path('movie_reviewer/', MovieReviewer.as_view(), name='movie_reviewer_url'),
    path("movie_reviewer/test/", actual_movie_reviewer_view, name='actual_movie_reviewer_url'),
    path('user_form_ai/', user_models_view, name='user_models_url'),
    path('face_protection/', FaceProtection.as_view(), name='face_protection_url'),
    path('face_protection/test', actual_face_protection_view, name='actual_face_protection_url'),

]
