from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy

from mytodo.models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'mytodo/list.html'

class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    initial = {'status':0}
    template_name = 'mytodo/create.html'
    success_url = reverse_lazy('mytodo:task-list')
