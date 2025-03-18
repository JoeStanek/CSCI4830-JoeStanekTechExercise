from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Task
from .forms import TaskForm
# Create your views here.

def front_page(request):
    return render(request, "front_page_css.html")

def about_page(request):
    return render(request, "about_page.html")

def view_task(request):
    page_number = request.GET.get("page",1)
    task = request.GET.get("task","").strip()
    date = request.GET.get("date","").strip()

    if request.method == "POST":
        task = request.POST.get("task","").strip()
        date = request.POST.get("date","").strip()
        page_number = 1
    
    if task or date:
        tasks = Task.object.filter(task_icontains=task, date_icontains=date)
    else:
        tasks = Task.objects.all()
    
    paginator = Paginator(tasks,10)
    page_obj = paginator.get_page(page_number)

    return render(
        request, "view_tasks.html",
        {"tasks":page_obj,
         "task_query": task,
         "date_query": date},
    )

def add_task(request):
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
        {"form":form, "added_task":added_task, "success":success},
    )


def edit_task():
    pass

def delete_task():
    pass