from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def update_profile(request):
    if request.method == 'POST':
        pass
    else:
        user = UserCreationForm()
    return render(request, 'profile.html' , {'user':user})