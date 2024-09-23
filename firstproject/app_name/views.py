from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def app_name(request):
    return HttpResponse("<h1> This is an Application </h1>")

def template_data(request):
    return render(request, "template1.html")