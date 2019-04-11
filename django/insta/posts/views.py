from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST,require_http_methods
from django.contrib.auth import get_user_model
from .forms import PostForm,CommentForm
from .models import post,Comment
# Create your views here.
def list(request,username):
    if username == "all":
        posts = post.objects.order_by('-id').all()
    else:
        people = get_object_or_404(get_user_model(),username=username)
        posts = post.objects.order_by('-id').filter(user=people)
    comment_form = CommentForm()
    return render(request,'posts/list.html',{'posts':posts,'comment_form':comment_form,'username':username})


@login_required
def create(request,username):
    # if request.user.is_authenticated()
    if request.method == 'POST':
        post_form = PostForm(data=request.POST,files=request.FILES)
        if post_form.is_valid():
            # post_form.save()
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()    # 실제 데이터베이스에 저장
            return redirect('posts:list',username)
    else:
        post_form = PostForm()
        return render(request,'posts/form.html',{'post_form':post_form})
        
@login_required        
def delete(request,username,post_id):
    # tmppost = post.objects.get(pk=post_id)
    tmppost = get_object_or_404(post,pk=post_id)
    if tmppost.user != request.user:
        return redirect('posts:list',username)
    tmppost.delete()
    return redirect('posts:list',username)

@login_required
def update(request,username,post_id):
    tmppost = get_object_or_404(post,id=post_id)
    if tmppost.user != request.user:
        return redirect('posts:list',username)
    if request.method == 'POST':
        post_form = PostForm(files=request.FILES,data=request.POST,instance=tmppost)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list',username)
    else:
        post_form = PostForm(instance=tmppost)
    return render(request,'posts/form.html',{'post_form':post_form})
    
@require_POST    
def comment_create(request,username,post_id):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
    return redirect('posts:list',username)

@require_http_methods(['GET','POST'])
def comment_delete(request,username,post_id,comment_id):
    comment = get_object_or_404(Comment,id=comment_id)
    if comment.user!=request.user:
        return redirect('posts:list',username)
    comment.delete()
    return redirect('posts:list',username)
    
@login_required(login_url='/accounts/all/login/')  
def like(request,username,post_id):
    tmppost = get_object_or_404(post,id=post_id)
    if not request.user in tmppost.like_users.all():
        # 1. 좋아요!
        tmppost.like_users.add(request.user)
    else:
        # 2. 좋아요 취소
        tmppost.like_users.remove(request.user)
    return redirect('posts:list',username)
    


    
    