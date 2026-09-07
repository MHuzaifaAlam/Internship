from django.urls import path
from .views import *

urlpatterns=[
    path("",TaskListView.as_view(),name="task_list"),
    path("<int:id>/",TaskDeleteView.as_view(),name="task_detail"),
    path("create/",TaskCreateView.as_view(),name="task_create"),
    path("update/<int:id>",TaskUpdateView.as_view(),name="task_update"),
    path("delete/<int:id>",TaskDeleteView.as_view(),name="delete_task"),
 
]