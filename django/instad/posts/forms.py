from django import forms
from .models import post,Comment,Image

class PostForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ['content',]
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['file',]
ImageFormset = forms.inlineformset_factory(post,Image,form=ImageForm,extra=3)

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'form-control','placeholder':'댓글을 작성하세요'}))
    class Meta:
        model = Comment
        fields = ['content',]