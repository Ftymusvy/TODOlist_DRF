from django.urls import path
from task.api.views import (
    task_list,
)

urlpatterns = [
    path('tasks/', task_list, name='task_list')
]
