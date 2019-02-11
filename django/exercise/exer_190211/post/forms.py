from django import forms
from .models import Food

class mainq(forms.Form):
    category = forms.CharField()
    
class PostModelForm(forms.ModelForm):
    category = forms.CharField()
    class Meta:
        model = Food
        fields = ['name','calorie','ingredients','category']