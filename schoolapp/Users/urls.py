from django.urls import path
from .views import studentloginpage, studentsignuppage, teacherloginpage, teachersignuppage, homepage

from .auth import student_signup_code

urlpatterns=[
    path('', homepage, name='homepage'),
    path('student/login/', studentloginpage, name='student-login'),
    path('student/signup/', studentsignuppage, name='student-signup'),
    path('teacher/login/', teacherloginpage, name='teacher-login'),
    path('teacher/signup/', teachersignuppage, name='teacher-signup'),
    path('student/signup/code/', student_signup_code, name='student-signup-code')
]