from django.urls import path
from . import views

urlpatterns=[
    path("",views.post_list,name="posts"),
    path("create",views.post_form,name="post_create"),
    path("<int:pk>/delete",views.post_delete,name="post_delete"),
    path("<int:pk>/update",views.post_update,name="post_update")
]