from django.shortcuts import render,redirect
from .models import Post,Comment
# Create your views here.

#def throw
#def catch
def new(request):
    if request.method == 'GET':
        return render(request,'new.html')
    else :
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        post = Post(title=title,content=content,image=image)
        post.save()
    
        return redirect('posts:detail',post.pk)
    
# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
#     image = request.FILES.get('image')
    
#     post = Post(title=title,content=content,image=image)
#     post.save()
    
#     return redirect('posts:detail',post.pk)
#     # return render(request,'create.html')

def index(request):
    # All post
    posts = Post.objects.all()
    
    return render(request,'index.html',{'posts':posts})
    
def detail(request,post_id):
    post = Post.objects.get(pk=post_id)
    # comments = post.comment_set.all()
    return render(request,'detail.html',{'post':post})
    
def naver(request,q):
    
    return redirect(f'https://search.naver.com/search.naver?query={q}')
    
def github(request,username):
    return redirect(f'https://github.com/{username}')
    
def delete(request,post_id):
    if request.method == 'POST':
        post = Post.objects.get(pk=post_id)
        # 삭제하는 코드
        post.delete()
        return redirect('posts:list')
    else:
        return render(request,'delete.html')

def edit(request,post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()
        return redirect('posts:detail',post.pk)
    else :
        return render(request,'edit.html',{'post':post})

# def update(request,post_id):
#     post = Post.objects.get(pk=post_id)
#     post.title = request.POST.get('title')
#     post.content = request.POST.get('content')
#     post.save()
#     return redirect('posts:detail',post.pk)
    
def comments_create(request,post_id):
    content=request.POST.get('content')
    post = Post.objects.get(pk=post_id)
    comment = Comment(post=post,content=content)
    comment.save()
    return redirect('posts:detail',post_id)

def comments_delete(request,post_id,comment_id):
    comment=Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('posts:detail',post_id)
    