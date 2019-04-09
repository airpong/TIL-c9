from django.shortcuts import render,redirect,get_object_or_404
from .forms import PostForm
from .models import post
# Create your views here.
def list(request):
    posts = post.objects.all()
    return render(request,'posts/list.html',{'posts':posts})
    
def create(request):
    if request.method == 'POST':
        post_form = PostForm(data=request.POST,files=request.FILES)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm()
        return render(request,'posts/create.html',{'post_form':post_form})
        
def delete(request,post_id):
    tmppost = post.objects.get(pk=post_id)
    tmppost = get_object_or_404(post,pk=post_id)
    tmppost.delete()
    return redirect('posts:list')
    
def update(request,post_id):
    tmppost = get_object_or_404(post,id=post_id)
    if request.method == 'POST':
        post_form = PostForm(files=request.FILES,data=request.POST,instance=tmppost)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=tmppost)
    return render(request,'posts/create.html',{'post_form':post_form})