from django.urls import path

from .views import TaskListView

app_name = 'mytodo'

urlpatterns = [
    path('',TaskListView.as_view(), name='task-list'),
]