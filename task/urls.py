from django.urls import path
from . import views

urlpatterns = [
    path('task/', views.TaskListView.as_view(), name="list-task"),

    path('task/create/', views.TaskCreateView.as_view(), name='create-task'),
    path('task/<int:pk>/delete/', views.DeleteTaskView.as_view(), name='delete-task'),
    path('task/<int:pk>/update/', views.UpdateTaskView.as_view(), name='update-task'),
]
