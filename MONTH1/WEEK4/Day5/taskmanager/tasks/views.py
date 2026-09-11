from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DetailView,TemplateView
from .models import Task
from .forms import TaskForm
from django.views import View
from django.shortcuts import redirect
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.generics import(
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

class TaskListView(LoginRequiredMixin,ListView):
    model=Task
    template_name="tasks/task_list.html"
    context_object_name="tasks"
    def get_queryset(self):
        task_filter=self.request.session.get(
            "task_filter",
            "my_tasks"
        )
        if task_filter == "all":
            return Task.objects.all()
        return Task.objects.filter(assigned_to=self.request.user)

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["current_filter"]=self.request.session.get("task_filter","my_tasks")
        return context
    


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

class TaskFilterView(View):
    def get(self,request,filter_type):
        request.session["task_filter"]=filter_type
        
        return redirect("task_list")

class TaskListAPIView(ListCreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer


class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=TaskSerializer
    def get_queryset(self):
        queryset=Task.objects.all()
        project_id=self.request.query_params.get("project")
        estimated_hours=self.request.query_params.get("hours")

        if project_id:
            queryset=queryset.filter(project_id=project_id)

        if estimated_hours:
            queryset=queryset.filter(estimated_hours__gte=estimated_hours)

        return queryset

    # def get(self,request,id):
    #     tasks=get_object_or_404(Task,id=id)
    #     serializer=TaskSerializer(tasks)
    #     return Response (serializer.data)

    
    # def put(self,request,id):
    #     task=get_object_or_404(Task,id=id)
    #     serializer=TaskSerializer(task,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=400)

    # def patch(self,request,id):
    #     task=get_object_or_404(Task,id=id)
    #     serializer=TaskSerializer(
    #         task,
    #         data=request.data,
    #         partial=True
    #         )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors,status=400)

    # def delete(self,request,id):
    #     task=get_object_or_404(Task,id=id)
    #     task.delete()
    #     return Response({"message":"Task Deleted Sucessfully"},status=204)
    
        
