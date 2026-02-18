from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        course = request.POST.get('course')
        email = request.POST.get('email')

        Student.objects.create(
            name=name,
            age=age,
            course=course,
            email=email
        )
        return redirect('home')

    return render(request, 'home.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'student_detail.html', {'student': student})