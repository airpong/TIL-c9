from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


# 1. Create
# post = Post(title='helo', content='world!') =>처음 post는 변수이름 뒤 Post 는 클래스이름
# post.save()

# 2. Read

# 2.1. All
# posts = Post.objects.all()

# 2.2 Get one
# post = Post.objects.get(pk=1)

# 2.3 filter
# posts = Post.objects.filter(title='hello')
# post = Post.objects.filter(title='hello').first()

# Like
# posts = Post.objects.filter(titl__contains='He').all()

# 2.5 order_by (정렬)
# posts = Post.objects.order_by('title').all() #=> 오름차순
# posts = Post.objects.order_by('-title').all() #=> 내림차순

# 2.6 limit & offset
# [offset:offset+limit]
# posts = Post.objects.all()[1:2]

# 3. Delete
# post = Post.objects.get(pk=2)
# post.delete()

# 4. Update
# post = Post.objects.get(pk=1)
# post.title = 'hi'
# post.save()