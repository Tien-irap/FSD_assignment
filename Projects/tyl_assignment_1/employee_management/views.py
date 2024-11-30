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
            request.session['logged_user'] = username
            return redirect("Dashboard Page")
        
        return render(request,'login_page.html', {'error_message': "Please Enter Correct Details"})
    
    return render(request,'login_page.html')

def logout_page(request):
    user = request.session['logged_user'] 
    del request.session['logged_user']

    return render(request,'logout_page.html',{'username':user})

def dashboard_page(request):
    username = request.session.get('logged_user', False) 
    if username:
        return render(request,'dashboard_page.html',{'username':username})
    
    return redirect("Login Page")

def employee_list_page(request):
    return render(request,'employee_list.html')