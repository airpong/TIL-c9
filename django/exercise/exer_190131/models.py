from django.db import models
# Create your models here.
class Movie(models.Model):
    titleKr = models.TextField()
    titleEn = models.TextField()
    spectators = models.IntegerField()
    summary = models.TextField()
    infourl = models.TextField()
    score = models.FloatField()
    poster = models.ImageField()
    picture1 = models.ImageField()
    picture2 = models.ImageField()
    picture3 = models.ImageField()
    genre = models.TextField(blank=True)