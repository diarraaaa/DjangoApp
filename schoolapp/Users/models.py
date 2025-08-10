from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    student_id=models.CharField(max_length=20,unique=True)
    level=models.CharField(max_length=10)
    departement=models.ForeignKey('Courses.Department',on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return f"{self.user.username} {self.student_id}"

class Teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    teacher_id=models.CharField(max_length=20,unique=True)
    subjects=models.ManyToManyField('Courses.Subject')
    departments=models.ManyToManyField('Courses.Department')
    
    def __str__(self):
        return f"{self.user.username} {self.teacher_id}"

class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    admin_id=models.CharField(max_length=10,unique=True)
    department=models.ForeignKey('Courses.Department',on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username} {self.admin_id}"
