from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
def postlist(request):
    posts = Post.objects.all()
    return render(request,'postlist.html',{'posts':posts})
    
@login_required    
def like(request,post_id):
    post = Post.objects.get(id=post_id)
    post.like_users.add(request.user)
    return redirect('posts:postlist')