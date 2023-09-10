from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(request, 'accounts/login.html', {'form': form, 'error': True})
        form_data = form.cleaned_data
        user = authenticate(request, username=form_data['username'], password=form_data['password'])
        if user is not None:
            if not user.is_active:
                return render(request, 'accounts/login.html', {'form': form, 'disabled': True})
            login(request, user)
            return HttpResponseRedirect(reverse('todolist:lobby'))
        else:
            return render(request, 'accounts/login.html', {'form': form, 'error': True})
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))


def user_register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if not user_form.is_valid():
            return render(request, 'accounts/register.html', {'form': user_form})
        new_user = user_form.save(commit=False)
        new_user.password = make_password(user_form.cleaned_data.get('password'))
        new_user.save()
        return render(request, 'accounts/register_completed.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': user_form})


def profile(request):
    return render(request, 'accounts/profile.html')