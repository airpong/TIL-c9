from django.shortcuts import render,redirect
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def new(request):
    return render(request,'new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    post = Post(title=title,content=content)
    post.save()
    return redirect('/post')

def detail(request,post_id):
    post = Post.objects.get(pk=post_id)
    return render(request,'detail.html',{'post':post})
    
def delete(request,post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('/post')
    
def edit(request,post_id):
    return render(request,'edit.html',{'post_id':post_id})
    
def confirm(request,post_id):
    post = Post.objects.get(pk=post_id)
    post.title = request.POST.get('title')
    post.content = request.POST.get('content')
    post.save()
    return redirect(f'/post/{post_id}/')
    