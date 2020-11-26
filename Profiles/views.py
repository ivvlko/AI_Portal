from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from Profiles.forms import CustomRegisterForm, UpdateUserForm, UpdateProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from Profiles.models import Profile


@transaction.atomic
def register_view(request):
    if request.method == 'GET':
        form = CustomRegisterForm()
        context = {
            'form': form
        }
        return render(request, 'profiles/register.html', context)

    else:
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            profile.user_id = user.id
            profile.save()
            group = Group.objects.get(name='regular_user')
            user.groups.add(group)
            messages.success(request, 'Account Created')
            return redirect('login_url')
        form = CustomRegisterForm(request.POST)
        context = {'form': form}
        return render(request, 'profiles/register.html', context)


@login_required()
def profile_view(request):
    if request.method == 'GET':
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        context = {'user_form': user_form, 'profile_form': profile_form,
                   'total_posts': len(request.user.news_set.all())}
        return render(request, 'profiles/profile.html', context)
    else:
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Account Successfully Updated')
            return redirect('profile_url')
