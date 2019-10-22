from django.urls import path

from .views import TaskListView, TaskCreateView

app_name = 'mytodo'

urlpatterns = [
    path('',TaskListView.as_view(), name='task-list'),
    path('create',TaskCreateView.as_view(), name='task-create'),
]