from pprint import pprint
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task
from django.shortcuts import render


@login_required
def lobby(request):
    tasks = Task.objects.filter(user=request.user).all()
    return render(request, 'todolist/lobby.html', {'tasks': tasks})


def create(request):
    redirect = HttpResponseRedirect(reverse('todolist:lobby'))
    if not request.method == 'POST':
        return redirect
    task_data = request.POST
    task = Task(user=request.user, title=task_data['title'], date_time=task_data.get('date_time'), done=False)
    task.save()
    return redirect


def mark(request):
    redirect = HttpResponseRedirect(reverse('todolist:lobby'))
    if not request.method == 'POST':
        return redirect
    marked = dict(request.POST)
    marked.pop('csrfmiddlewaretoken')
    if not marked:
        return redirect
    marked_ids = [int(mark_id) for mark_id in marked.keys()]
    marked_tasks = Task.objects.filter(pk__in=marked_ids)
    for marked_task in marked_tasks:
        if marked_task.done:
            marked_task.done = False
        else:
            marked_task.done = True
        marked_task.save()
    return redirect
