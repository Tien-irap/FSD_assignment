from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def app_data(request):
    return HttpResponse("<h1>This is App1 data</h1>")

def template_data(request):
    name = 'CMRIT'
    return render(request, 'template1.html', {"backend_data": name,"array":['ABC','DEF','GHI']})