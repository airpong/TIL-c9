# Create your models here.
from django.db import models
from django.core.validators import EmailValidator,MinValueValidator

class Person(models.Model):
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100,validators=[EmailValidator(message='안맞음나랑')])
	age = models.IntegerField(validators=[MinValueValidator(20,message="미성년자 ㄴㄴ")])