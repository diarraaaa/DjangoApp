from django.db import models


# Create your models here.
class Subject(models.Model):
    coursename=models.CharField(max_length=50,unique=True)
    credits=models.IntegerField()
    coefficient=models.IntegerField()
    code=models.CharField(max_length=20,unique=True)
    description=models.TextField()
    
    def __str__(self):
        return f"{self.coursename} {self.description}"
    
class Course(models.Model):
    title=models.TextField()
    description=models.TextField()
    subject=models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True)
    professor=models.ForeignKey('Users.Teacher',on_delete=models.SET_NULL,null=True)
    upload_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title}"
    
class Exercise(models.Model):
    types=[('exam','Exam'),('exercise','Exercise'),('quiz','Quiz')]
    title=models.TextField()
    description=models.TextField()
    subject=models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True)
    professor=models.ForeignKey('Users.Teacher',on_delete=models.SET_NULL,null=True)
    upload_date=models.DateTimeField(auto_now_add=True)
    due_date=models.DateTimeField()
    type=models.CharField(max_length=10,choices=types)
    points=models.IntegerField()
    
    def __str__(self):
        return f"{self.title}"
    
class Department(models.Model):
    name=models.CharField(max_length=20,unique=True)
    chief_name=models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"