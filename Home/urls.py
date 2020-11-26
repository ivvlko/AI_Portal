from django.urls import path
from Home.views import HomePageView, AboutPageView, SearchResults

urlpatterns = [
    path('', HomePageView.as_view(), name='home_url'),
    path('about/', AboutPageView.as_view(), name='about_url'),
    path('results/', SearchResults.as_view(), name='search_url')
]
