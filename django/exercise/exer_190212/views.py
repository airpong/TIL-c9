from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save()
            return redirect('settings:profile')
    else:
        user = UserCreationForm()
    return render(request, 'profile.html' , {'user_form':user_form,'profile_form':profile_form})