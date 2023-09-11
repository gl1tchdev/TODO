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
    output = {}
    if request.method == 'GET':
        form = UpdateUserForm(initial={'username': request.user.username, 'email': request.user.email})
        output.update({'form': form})
    else:
        form = UpdateUserForm(request.POST)
        output.update({'form': form})
        if not form.is_valid():
            output.update({'error': 'Form data is invalid'})
            return render(request, 'accounts/profile.html', output)
        cleaned_data = form.cleaned_data
        if not request.user.check_password(cleaned_data.get('password')):
            output.update({'error': 'Old password is wrong'})
            return render(request, 'accounts/profile.html', output)
        if cleaned_data.get('username') != request.user.username:
            request.user.username = cleaned_data.get('username')
        if cleaned_data.get('email') != request.user.email:
            request.user.email = cleaned_data.get('email')
        request.user.save()
        if cleaned_data.get('new_password'):
            request.user.password = make_password(cleaned_data.get('new_password'))
            request.user.save()
            return HttpResponseRedirect(reverse('accounts:login'))
    return render(request, 'accounts/profile.html', output)


def tg_connect(request):
    return render(request, 'accounts/tg_connect.html')