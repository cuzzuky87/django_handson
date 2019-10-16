from django.shortcuts import render
from django.views.generic import ListView

from mytodo.models import Task

class TaskListView(ListView):
    model = Task
    template = 'mytodo/list.html'