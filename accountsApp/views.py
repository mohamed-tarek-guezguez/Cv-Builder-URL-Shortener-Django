from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = CreateUserForm()

    context = {
        'title': 'Sign up',
        'form': form,
    }

    return render(request, 'register.ejs', context)

@login_required
def profile(request):
    context = {
        'title': 'Profile',
    }
    return render(request, 'profile.ejs', context)

@login_required
def settings(request):

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'title': 'Settings',
        'p_form': p_form,
    }
    return render(request, 'settings.ejs', context)
