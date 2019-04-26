from django.shortcuts import render
from .models import Post
# Create your views here.
def postlist(request):
    posts = Post.objects.all()
    return render(request,'postlist.html',{'posts':posts})
    
