from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Task, Notification
from django.shortcuts import render
from .tasks import notify_user
from TODO.utils import get_datetime_obj



@login_required
def lobby(request, page=1):
    tasks = Task.objects.filter(user=request.user).order_by('id').reverse().all()
    p = Paginator(tasks, 7)
    try:
        tasks = p.page(page)
    except EmptyPage:
        tasks = p.page(1)
    return render(request, 'todolist/lobby.html',
                  {'tasks': tasks.object_list, 'current_page': page, 'has_next_page': tasks.has_next(),
                   'has_prev_page': tasks.has_previous(), 'tasks_p': tasks})


def create(request):
    response = HttpResponseRedirect(reverse('todolist:lobby'))
    if not request.method == 'POST':
        return response
    task_data = request.POST
    task = Task(user=request.user, title=task_data['title'], done=False)
    if task_data.get('date_time'):
        notification = Notification(date_time=task_data.get('date_time'))
        notification.save()
        task.notification = notification
        task.save()
        datetime = get_datetime_obj(task.notification.date_time)
        notify_user.apply_async(args=(request.user.id, task.id), eta=datetime, soft_time_limit=10, time_limit=10)
    task.save()
    return response


def mark(request):
    redirect = HttpResponseRedirect(reverse('todolist:lobby'))
    if not request.method == 'POST':
        return redirect
    marked = dict(request.POST)
    marked.pop('csrfmiddlewaretoken')
    current = marked.pop('current_page')[0]
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
    redirect['location'] += str(current)
    return redirect


def delete(request, task_id):
    redirect = HttpResponseRedirect(reverse('todolist:lobby'))
    Task.objects.filter(pk=task_id).delete()
    return redirect
