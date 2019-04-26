from django.shortcuts import render,redirect,get_object_or_404
from .forms import CustomUserCreationForm,CustonUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.conf import settings
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.method == "GET":
        form = CustomUserCreationForm()
        return render(request,'forms.html',{'form':form})
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect('posts:postlist')
            
def logout(request):
    auth_logout(request)
    return redirect('posts:postlist')
    
def login(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request,'forms.html',{'form':form})
    else:
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
        return redirect('posts:postlist')
@login_required        
def userlist(request):
    users = get_user_model().objects.all()
    return render(request,'userlist.html',{'users':users})
@login_required  
def userdetail(request,username):
    user = get_object_or_404(get_user_model(),username=username)
    return render(request,'userdetail.html',{'user':user})
    
@login_required  
def follow(request,username):
    targetuser = get_object_or_404(get_user_model(),username=username)
    if request.user in targetuser.followers.all():
        targetuser.followers.remove(request.user)
        return redirect('accounts:userdetail',username)
    else:
        targetuser.followers.add(request.user)
        return redirect('accounts:userdetail',username)
        
def update(request,username):
    targetuser = get_object_or_404(get_user_model(),username=username)
    if request.method=="GET":
        form = CustonUserChangeForm(instance=targetuser)
        return render(request,'forms.html',{'form':form})
    else:
        form = CustonUserChangeForm(request.POST,instance=targetuser)
        if form.is_valid():
            user = form.save()
            return redirect('accounts:userdetail',user.username)
@login_required
def password(request,username):
    targetuser = get_object_or_404(get_user_model(),username=username)
    if request.method == "GET":
        form = PasswordChangeForm(request.user)
        return render(request,'forms.html',{'form':form})
    else:
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            return redirect('accounts:userdetail',request.user.username)