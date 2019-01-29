from django.shortcuts import render,redirect
from .models import Student
from .models import Post

# Create your views here.
def index(request):
    students = Student.objects.all()
    posts = Post.objects.all()
    return render(request,'index.html',{'students':students,'posts':posts})
    
def new(request):
    return render(request,'new.html')
    
def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    birthday = request.POST.get('birthday')
    age = request.POST.get('age')
    student = Student(name=name,email=email,birthday=birthday,age=age)
    student.save()
    return redirect('/post')
    
def detail(request,student_id):
    student = Student.objects.get(pk=student_id)
    return render(request,'detail.html',{'student':student})
    
def delete(request,student_id):
    student = Student.objects.get(pk=student_id)
    student.delete()
    return redirect('/post')
    
def update(request,student_id):
    return render(request,'update.html',{'student_id':student_id})
    
def confirm(request,student_id):
    student = Student.objects.get(pk=student_id)
    student.name = request.POST.get('name')
    student.email = request.POST.get('email')
    student.birthday = request.POST.get('birthday')
    student.age = request.POST.get('age')
    student.save()
    return redirect(f'/post/{student_id}')
    
def search(request):
    name = request.POST.get('name')
    students = Student.objects.filter(name=name).all()
    return render(request,'showall.html',{'students':students})
    
def postit(request,student_name):
    return render(request,'postit.html',{'student_name':student_name})
    
def messageconfirm(request,student_name):
    message=request.POST.get('message')
    name = student_name
    post = Post(name=name,message=message)
    post.save()
    return redirect('/post')