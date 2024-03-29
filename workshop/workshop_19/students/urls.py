from django.contrib import admin
from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('<int:pk>/', views.detail, name="detail"),
]