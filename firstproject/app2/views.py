from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def app_data(request):
    return(HttpResponse("<h1>This is App2 Data</h1>"))