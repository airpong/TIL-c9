from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.
# def post_image_path(instance,filename) :
#     return f'image/{instance.post.user.username}/{instance.post_id}/{filename}'
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=40,blank=True)
    introduction = models.TextField(blank=True)
    image = ProcessedImageField(
            blank = True,
            upload_to = 'profile/images', #저장위치
            processors=[ResizeToFill(600,600)],# 처리할 작업 목록
            format='JPEG',#포맷 저장
            options={'quality':90},#옵션
        )

class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')