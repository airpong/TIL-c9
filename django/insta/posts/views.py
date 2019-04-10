from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import post
# Create your views here.
def list(request):
    posts = post.objects.order_by('-id').all()
    return render(request,'posts/list.html',{'posts':posts})


@login_required
def create(request):
    # if request.user.is_authenticated()
    if request.method == 'POST':
        post_form = PostForm(data=request.POST,files=request.FILES)
        if post_form.is_valid():
            post_form.save()
            post = post_form.save(commit=False)
            post.user = request.user
            post.save()    # 실제 데이터베이스에 저장
            return redirect('posts:list')
    else:
        post_form = PostForm()
        return render(request,'posts/form.html',{'post_form':post_form})
        
def delete(request,post_id):
    # tmppost = post.objects.get(pk=post_id)
    tmppost = get_object_or_404(post,pk=post_id)
    if tmppost.user != request.user:
        return redirect('posts:list')
    tmppost.delete()
    return redirect('posts:list')


def update(request,post_id):
    tmppost = get_object_or_404(post,id=post_id)
    if tmppost.user != request.user:
        return redirect('posts:list')
    if request.method == 'POST':
        post_form = PostForm(files=request.FILES,data=request.POST,instance=tmppost)
        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')
    else:
        post_form = PostForm(instance=tmppost)
    return render(request,'posts/form.html',{'post_form':post_form})