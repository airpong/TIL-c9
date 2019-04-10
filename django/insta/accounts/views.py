from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here. 
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method=='GET':
        signup_form = UserCreationForm()
        return render(request,'accounts/signup.html',{'signup_form':signup_form})
    elif request.method == "POST":
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
        return redirect('posts:list')

def login(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request,request.POST)

        # login_form = AuthenticationForm(None,request.POST)
        
        # login_form = AuthenticationForm(data = request.POST)


        if login_form.is_valid():
            auth_login(request,login_form.get_user())
            return redirect(request.GET.get('next') or 'posts:list')
        else:
            message="다시 확인하세요."
            return render(request,'accounts/login.html',{'login_form':login_form,'message':message})
    else:
        login_form = AuthenticationForm()
        message = "로그인 하세요."
        return render(request,'accounts/login.html',{'login_form':login_form,'message':message})
        
def logout(request):
    auth_logout(request)
    return redirect('posts:list')
    