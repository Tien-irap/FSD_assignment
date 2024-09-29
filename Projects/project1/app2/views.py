from django.http import HttpResponse
from django.shortcuts import render

def app_data(request):
    return HttpResponse("<h1>This is App2 Data</h1>")