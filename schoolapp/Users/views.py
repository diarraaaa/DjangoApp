from django.shortcuts import render

# Create your views here.
def studentloginpage(request):
    return render(request, 'auth/studentlogin.html')
def studentsignuppage(request):
    return render(request, 'auth/studentsignup.html')
def teacherloginpage(request):
    return render(request, 'auth/teacherlogin.html')
def teachersignuppage(request):
    return render(request, 'auth/teachersignup.html')
def homepage(request):
    return render(request, 'auth/homepage.html')