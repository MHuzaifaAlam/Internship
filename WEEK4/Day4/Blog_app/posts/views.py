from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404

def post_list(request):
    posts=Post.objects.all()
    return render(request,"posts/post_list.html",{"posts":posts})

def post_form(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form = PostForm()

    return render(request, "posts/post_form.html", {"form": form})

def post_delete(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("posts")
    return render(request,"posts/post_confrim_delete.html",{"post":post})

def post_update(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts")
    else:
        form=PostForm(instance=post)
    return render(request,"posts/post_form.html",{"form":form})


