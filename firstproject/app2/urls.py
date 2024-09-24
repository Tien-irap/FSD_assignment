from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('app_name/', views.app_data),
    path('data/', views.app_data, name = "Appplication 2"),
]