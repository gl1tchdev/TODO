from pprint import pprint

from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
from django.shortcuts import render


def lobby(request):
    return render(request, 'todolist/lobby.html')


def create(request):
    redirect = HttpResponseRedirect(reverse('todolist:lobby'))
    if not request.method == 'POST':
        return redirect
    task_data = request.POST
    task = Task(user=request.user, title=task_data['title'], date_time=task_data.get('date_time'), done=False)
    task.save()
    return redirect
