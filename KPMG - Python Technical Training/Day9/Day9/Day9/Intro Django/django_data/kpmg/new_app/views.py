from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#http://127.0.0.1:8000//app/index
def index(request):
    return HttpResponse("<h1>Hello World ,This is my First application new_app!</h1>")
