from django.urls import path
from .views import task_list,task_detail,task_create,task_update,delete_task
urlpatterns=[
    path("",task_list,name="task_list"),
    path("<int:id>/",task_detail,name="task_detail"),
    path("create/",task_create,name="task_create"),
    path("update/<int:id>",task_update,name="task_update"),
    path("delete/<int:id>",delete_task,name="delete_task")
]