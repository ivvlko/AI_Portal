from django.shortcuts import render


def models_home(request):
    return render(request, 'models/models_home.html')
