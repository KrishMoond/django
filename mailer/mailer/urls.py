from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('send-email/', views.send_email, name='send_email'),

]
