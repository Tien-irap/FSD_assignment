from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('app_name/', views.app_name),
    path('data/', views.app_name, name = "Appplication 1"),
    path('templates/', views.template_data, name = "Template Data")
]