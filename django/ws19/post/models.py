from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    birthday = models.DateField(max_length=100)
    age = models.IntegerField()
    
class Post(models.Model):
    name = models.CharField(max_length=100)
    message=models.TextField()