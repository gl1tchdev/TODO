from django.shortcuts import render
from .forms import searchForm


def lobby(request):
    form = searchForm()
    return render(request, 'todolist/lobby.html', {'form': form})


def search(request):
    return render(request, 'todolist/lobby.html')
