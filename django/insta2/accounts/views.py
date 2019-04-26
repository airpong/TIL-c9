from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
def userlist(request):
    users = get_user_model().objects.all()
    return render(request,'userlist.html',{'users':users})
    
def signup(request):
    if request.method == "GET":
        user_form = UserCreationForm()
        return render(request,'forms.html',{'user_form':user_form})
    else:
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request,user)
        return redirect('accounts:userlist')
        
def login(request):
    if request.method == "GET":
        login_form = AuthenticationForm()
        return render(request,'forms.html',{'user_form':login_form})
    else:
        login_form = AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            auth_login(request,login_form.get_user())
            return redirect('accounts:userlist')
            
