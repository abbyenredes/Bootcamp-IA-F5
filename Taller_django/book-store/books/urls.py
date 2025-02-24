from django.contrib import admin
from django.urls import path
from .views import GetAllBook

urlpatterns = [
    path('', GetAllBook, name='books'), 
]