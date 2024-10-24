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

def handle_submit(request):
    if request.method == 'POST':
        formData = request.POST.get('inputData')
        return HttpResponse(f"Data Received from frontend is, {formData}")
    return render(request,'form_template.html')

def signup_form(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if(len(username) == 0 or len(password) == 0):
            return HttpResponse(f"Error, Go back Enter something")
        
        print(f"Password is: {password}")
        return HttpResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Signup Sucess</title>
</head>

<style>
    body{
        background-color: blue;
        background-size: cover;
        font-family: Arial, sans-serif;
    }

    .container{
        width: 20vw;
        background-color: #fff;
        margin: 10% 40vw;
        padding: 20px;
        border-radius: 10px;
    }

    h3{
        margin: 10px 0 10px 0;
        text-align: center;
    }
</style>

<body>
    <div class="container">
        <h3>Sucessful Signup<br>
        Welcome, signed_user</h3>
    </div>
</body>
</html>""".replace('signed_user',username))
    return render(request,'signup/form.html')