from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    return HttpResponse("Hello, world! This is Joe Staneks CSCI4830 Tech Excercise base django webpage.")

