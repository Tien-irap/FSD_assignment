from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import login_details
import random

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        #Get Data from the fields
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Register
        # login_details.insert_one({'f_sno':random.getrandbits(63),'f_userName':username,'f_Pwd':password})
        
        # Find Directory
        response = login_details.find_one({'f_userName':username})
        if response and response['f_Pwd'] == password:
            request.session['logged_in'] = True
            return redirect("Dashboard Page")
        
        return render(request,'login_page.html', {'error_message': "Please Enter Correct Details"})
    
    return render(request,'login_page.html')

def dashboard_page(request):
    if not request.session.get('logged_in', False):
        return redirect("Login Page")
    
    return render(request,'dashboard_page.html')