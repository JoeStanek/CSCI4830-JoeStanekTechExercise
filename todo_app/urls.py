from django.urls import path
from .views import front_page
from .views import add_task
from .views import edit_task
from .views import view_task
from .views import delete_task



urlpatterns = [
    path("", front_page, name="front_page"),
    path("view/",view_task,name="view_task"),
    path("add/",add_task, name="add_task"),
    path("edit_task/<int:task_id>/<int:page_number/", edit_task, name="edit_task",),
    path("delete_task/<int:task_id>/<int:page_number/", delete_task, name="delete_task",),
]