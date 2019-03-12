from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})
    
def new(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        birthday = request.POST.get('birthday')
        age = request.POST.get('age')
        student = Student(name=name, email=email, birthday=birthday, age=age)
        student.save()
        return redirect('students:index')
    else:
        return render(request, 'students/new.html')

def detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'students/detail.html', {'student':student})