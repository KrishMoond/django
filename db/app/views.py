from django.shortcuts import render, redirect
from .models import Student

def home(request):
    return render(request, 'app/home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'app/student_list.html', {'students': students})
