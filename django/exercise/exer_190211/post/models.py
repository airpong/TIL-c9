from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    calorie = models.IntegerField()
    ingredients = models.TextField()
    category = models.CharField(max_length=100)