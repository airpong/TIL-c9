from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()


# 정리  
# class Post : / in_Django - Model / in_DB - Table / 
# post = Post() : / in_Django - Instance or Object / in_DB - Record or Row
# title : / in_Django - Field / in_DB - Column

# 1.create
# 방법1
# post1 = Post(title='hello')
# post1.save()

# 방법2
# post2 = Post.objects.create(title = 'hello-2')

# 방법3
# post3 = Post()
# post3.title = 'hello-3'
# post3.save()
# post3.title = 'hello!!!'
# post3.save()

# 2. Read

# 2-1. All
# posts = Post.object.all()

# 2-2. one or many
# posts = Post.object.get(id=1)     -단 한개만 가져옴

# posts = Post.object.get(title='hello2')

# posts = get_object_or_404(Post,title='hello2')

# post = Post.objcets.filter(pk=1)[0]   -filter 는 조건을 만족시키는 객체의 리스트 반환
# post = Post.objects.filter(pk=1).first()

# 2-3 Where(filter)
# posts = Post.objects.filter(title='hello-1')
# post = Post.objects.filter(title='hello-1').first()
