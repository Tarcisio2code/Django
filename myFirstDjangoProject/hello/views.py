
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def viewTwo(request):
    return HttpResponse("This is the second view")

def viewThree(request):
    return HttpResponse("This is the third view")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })
