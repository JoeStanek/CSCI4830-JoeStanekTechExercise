from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm
# Create your views here.

def front_page():
    pass

def view_task():
    pass

def add_task(request):
    print("[DBG] add_task called.")
    success = False
    added_task = None
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            success = True
            added_task = new_task
            return render(
                request,
                "add_task.html",
                {"form":form, "added_task":added_task, "success":success},
            )
        else:
            form = TaskForm()
        return render(
            request,
            "add_task.html",
            {"form":form, "added_task":added_task, "success":success}
        )


def edit_task():
    pass

def delete_task():
    pass