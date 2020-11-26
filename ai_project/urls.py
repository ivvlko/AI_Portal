from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls, name='admin_url'),
    path('', include('Home.urls')),
    path('news/', include('NewsSection.urls')),
    path('users/', include('Profiles.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='profiles/login.html'), name='login_url'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/home.html'), name='logout_url'),
    path('models/', include('Models.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


