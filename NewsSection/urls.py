from django.urls import path
<<<<<<< HEAD
from NewsSection.views.add_news import add_news_view
from NewsSection.views.all_news import AllNews
from NewsSection.views.all_news_by_user import all_news_by_user_view
from NewsSection.views.computer_vision import CvView
from NewsSection.views.delete_news import delete_view
from NewsSection.views.details import details_view
from NewsSection.views.nlp import NLPView
from NewsSection.views.robotics import RoboticsView
from NewsSection.views.update import update_view


urlpatterns = [
    path('computer_vision/', CvView.as_view(), name='computer_vision_url'),
    path('details/<int:pk>/', details_view, name='details'),
    path('natural_language_processing/', NLPView.as_view(), name='nlp_url'),
    path('robotics/', RoboticsView.as_view(), name='robotics_url'),
    path('all_news/', AllNews.as_view(), name='all_news_url'),
    path('add_news/', add_news_view, name='add_news_url'),
    path('user_news/', all_news_by_user_view, name='all_news_by_user_url'),
    path('update/<int:pk>', update_view, name='update_url'),
    path('delete/<int:pk>', delete_view, name='delete_url'),
=======
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
>>>>>>> 10c795f36d23a00f8ab4fec4346b45eac822fd47

]