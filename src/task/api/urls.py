from django.urls import path
from task.api.views import (
    task_list,
    api_task_detail,
    api_task_update
)

urlpatterns = [
    path('tasks/', task_list, name='task_list'),
    path('task/<int:id>' , api_task_detail , name ='task-detail'),
    path('task/<int:pk>/update' , api_task_update , name ='task-update')
]
