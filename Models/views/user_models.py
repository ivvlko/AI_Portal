from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from Models.forms import UserModelForm


@login_required()
def user_models_view(request):
    if request.method == 'GET':
        form = UserModelForm()
        context = {'form': form}
        return render(request, 'models/user_models_form.html', context)
    else:
        form = UserModelForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.sender_id = request.user.id
            obj.save()
            messages.success(request, "Thank You. We'll Contact You as soon as Possible!")
            return redirect('models_home_url')
        context = {'form': form}
        return render(request, 'models/user_models_form.html', context)
