from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Student, Teacher
from django.contrib.auth.models import User
from Courses.models import Department

def student_signup_code(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        department=request.POST.get('department')
        department=Department.objects.get(name=department)
        if not department:
            department.save()
        level=request.POST.get('level')
        student_id=request.POST.get('student_id')
        password=request.POST.get('password1')
        password2=request.POST.get('password2')
        if not(password == password2):
            return render(request, 'auth/studentsignup.html', {'error': 'Passwords do not match.'})
        user=authenticate(username=username, password=password)
        if user is not None:
            return render(request, 'auth/studentsignup.html', {'error': 'Username already exists.'})
        else:
            user=User.objects.create_user(username=username, email=email, password=password)
            student=Student.objects.create(user=user, department=department, level=level, student_id=student_id)
            student.save()
            return render(request, 'auth/studentsignup.html', {'success': 'Account created successfully.'})
    return render(request, 'auth/studentsignup.html')