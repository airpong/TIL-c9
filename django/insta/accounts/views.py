from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from posts.forms import CommentForm
from posts.models import post
# Create your views here. 
def signup(request,username):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method=='GET':
        signup_form = UserCreationForm()
        return render(request,'accounts/signup.html',{'signup_form':signup_form})
    elif request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        print("Abcd")
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('posts:list',username)

def login(request,username):
    if request.user.is_authenticated:
        return redirect('posts:list',username)
    if request.method == 'POST':
        login_form = AuthenticationForm(request,request.POST)

        # login_form = AuthenticationForm(None,request.POST)
        
        # login_form = AuthenticationForm(data = request.POST)


        if login_form.is_valid():
            auth_login(request,login_form.get_user())
            return redirect(request.GET.get('next') or 'posts:list' , username)
        else:
            message="다시 확인하세요."
            return render(request,'accounts/login.html',{'login_form':login_form,'message':message})
    else:
        login_form = AuthenticationForm()
        message = "로그인 하세요."
        return render(request,'accounts/login.html',{'login_form':login_form,'message':message})
        
def logout(request,username):
    auth_logout(request)
    return redirect('posts:list',username)
    
def people(request,username):
    # get_user_model() #->return user class 
    people = get_object_or_404(get_user_model(),username=username)
    posts = post.objects.filter(user=people)
    comment_form = CommentForm()
    return render(request,'posts/list.html',{'posts':posts,'comment_form':comment_form})
    # return render(request, 'accounts/people.html',{'people':people})