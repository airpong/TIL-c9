from django import forms
from django.contrib.auth.forms import UserChangeForm,UserCreationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
        
class CustonUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['username']