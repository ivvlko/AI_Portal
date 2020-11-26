from django.urls import path
from NewsSection.views.all_news import AllNews
from NewsSection.views.computer_vision import CvView
from NewsSection.views.details import details_view
from NewsSection.views.nlp import NLPView
from NewsSection.views.robotics import RoboticsView

urlpatterns = [
    path('computer_vision/', CvView.as_view(), name='computer_vision_url'),
    path('details/<int:pk>/', details_view, name='cv_details_url'),
    path('natural_language_processing/', NLPView.as_view(), name='nlp_url'),
    path('robotics/', RoboticsView.as_view(), name='robotics_url'),
    path('all_news/', AllNews.as_view(), name='all_news_url'),

]