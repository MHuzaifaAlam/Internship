from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView
from .models import Task
from .forms import TaskForm
class TaskListView(LoginRequiredMixin,ListView):
    model=Task
    template_name="tasks/task_list.html"
    context_object_name="tasks"
    def get_queryset(self):
        return Task.objects.filter(assigned_to=self.request.user)


class TaskDetailView(DetailView):
    model=Task
    template_name="tasks/task_detail.html"
    context_object_name="tasks"
    pk_url_kwarg="id"

class TaskCreateView(CreateView):
    model=Task
    form_class=TaskForm
    template_name="tasks/task_create.html"
    sucess_url=reverse_lazy("task_list")

class TaskUpdateView(UpdateView):
    model=Task
    form_class=TaskForm
    template_name="tasks/task_update.html"
    pk_url_kwarg="id"
    success_url=reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model=Task
    template_name="tasks/delete_task.html"
    context_object_name="tasks"
    pk_url_kwarg="id"
    success_url=reverse_lazy("task_list")


    

