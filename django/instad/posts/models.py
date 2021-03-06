from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

def post_image_path(abc, filename):
    return f'posts/{filename}'
    

# Create your models here.
class post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_posts')

class Image(models.Model):
    Post = models.ForeignKey(post, on_delete=models.CASCADE)
    file = ProcessedImageField(
                    upload_to = post_image_path,     # 저장 위치
                    processors =[ResizeToFill(600,600)],    # 처리할 작업 목록
                    format='JPEG',  # 저장 포맷
                    options={'quality':90}, # 옵션
                )
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    post = models.ForeignKey(post,on_delete=models.CASCADE)
    content = models.TextField()
    
