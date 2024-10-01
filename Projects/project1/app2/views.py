from django.http import HttpResponse
from django.shortcuts import render
import requests
import json 

def app_data(request):
    return HttpResponse("<h1>This is App2 Data</h1>")

def rest_api_data(request):
    res = requests.get('http://jsonplaceholder.typicode.com/comments')
    data = json.loads(res.text)
    return render(request,'template3.html',{"data":data})