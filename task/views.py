from django.views import generic
from .models import Task
from django.urls import reverse_lazy
from .forms import TaskForm

# Create your views here.

class TaskListView(generic.ListView):
    template_name = 'task/task_list.html'
    model = Task
    context_object_name = 'task'


class TaskCreateView(generic.CreateView):
    template_name = 'task/task_create.html'
    model = Task
    context_object_name = 'Task'
    form_class = TaskForm
    success_url = reverse_lazy('list-task') 


class DeleteTaskView(generic.DeleteView):
    template_name = 'task/task_confirm_delete.html'
    model = Task
    context_object_name = 'Task'
    success_url = reverse_lazy('list-task')

class UpdateTaskView(generic.UpdateView):
    template_name = 'task/task_confirm_update.html'
    model = Task
    context_object_name = 'Task'
    form_class = TaskForm
    success_url = reverse_lazy('list-task')

