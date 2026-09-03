from django.shortcuts import render,get_object_or_404,redirect
from .models import Task,Project

def task_list(request):
    tasks=Task.objects.all()

    return render(request,"tasks/task_list.html",{
        "tasks":tasks
    })

def task_detail(request,id):
    task=get_object_or_404(Task,id=id)
    return render(request,"tasks/task_detail.html",{
        "task":task
        })

def task_create(request):
    if request.method == "POST":
        title=request.POST.get("title")
        description=request.POST.get("description")
        project=Project.objects.first()
        Task.objects.create(
            title=title,
            description=description,
            project=project
        )
        return redirect("task_list")
    return render(request,"tasks/task_create.html")

def task_update(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=="POST":
        task.title=request.POST.get("title")
        task.description=request.POST.get("description")
        task.save()
        return redirect("task_list")
    return render(request,"tasks/task_update.html",{
        "task":task
    })

def delete_task(request,id):
    task=get_object_or_404(Task,id=id)
    if request.method=="POST":
        task.delete()
        return render("task_list")
    return render(request,"delete_task.html",{
        "task":task
    })


    

