from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.login_page, name="Login Page"),
    path('dashboard/', views.dashboard_page, name="Dashboard Page"),
    path('employee_list/',views.employee_list_page,name="Employee List Page"),
    path('create_employee/',views.employee_create_page,name="Create Employee Page"),
    path('logout/',views.logout_page,name="Logout Page")
]