from django.shortcuts import render,redirect
from .models import Question,Choice
# Create your views here.
def index2(request):
    questions = Question.objects.all()
    return render(request,'index2.html',{'questions':questions})
    
def newChoice(request,question_id):
    return render(request,'newChoice.html')
    
def upload(request,question_id):
    question=Question.objects.get(pk=question_id)
    content = request.POST.get('content')
    choice = Choice(question=question,content=content,votes=0)
    choice.save()
    return redirect('exer_190130:list')
    
def submit(request,question_id,menu_id):
    menu = Choice.objects.get(pk=menu_id)
    question = Question.objects.get(pk=question_id)
    menu.votes +=1
    menu.save()
    return render(request,'resultpage.html',{'question':question})
    
def newquestion(request):
    return render(request,'newquestion.html')
    
def createquestion(request):
    title=request.POST.get('title')
    question=Question(title=title)
    question.save()
    return redirect('exer_190130:list')
    

    