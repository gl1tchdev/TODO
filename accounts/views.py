from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .forms import LoginForm, UserRegistrationForm, UpdateUserForm


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
    if request.method == 'GET':
        form = UpdateUserForm(initial={'username': request.user.username, 'email': request.user.email})
    else:
        form = UpdateUserForm(request.POST)
        if not form.is_valid():
            return render(request, 'accounts/profile.html', {'form': form, 'error': 'Form data is invalid'})
        cleaned_data = form.cleaned_data
        user = authenticate(request, username=request.user.username, password=cleaned_data.get('password'))
        if not user:
            return render(request, 'accounts/profile.html', {'form': form, 'error': 'Old password is wrong'})
        if cleaned_data.get('username'):
            request.user.username = cleaned_data.get('username')
            request.user.save()
        if cleaned_data.get('email'):
            request.user.email = cleaned_data.get('email')
            request.user.save()
        if cleaned_data.get('new_password'):
            request.user.password = make_password(cleaned_data.get('new_password'))
            request.user.save()
            return HttpResponseRedirect(reverse('accounts:login'))
    return render(request, 'accounts/profile.html', {'form': form, 'success': 'Congrats, info changed'})
