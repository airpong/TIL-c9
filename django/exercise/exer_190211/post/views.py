from django.shortcuts import render,redirect
from .forms import mainq,PostModelForm
from .models import Food
# Create your views here.
def index(request):
    if request.method=="POST":
        form = mainq(request.POST)
        if form.is_valid():
            category = form.cleaned_data.get('category')
            foods = Food.objects.filter(category=category)
            return render(request,'list.html',{'foods':foods,'category':category})
    else:
        mainqs = mainq()
    
    return render(request,'index.html',{'mianq':mainqs})
    
def create(request,category):
    if request.method=="POST":
        form = PostModelForm(request.POST)
        if form.is_valid():
            food = form.save()
            foods = Food.objects.filter(category=food.category)
            return render(request,'list.html',{'foods':foods,'category':food.category})
    else:
        form = PostModelForm(initial={'category':category})
    return render(request,'create.html',{'form':form,'category':category})
    
def detail(request,food_id):
    if request.method=='POST':
        category = request.POST.get('category')
        foods = Food.objects.filter(category=category)
        return render(request,'list.html',{'foods':foods,'category':category})
    else:
        food = Food.objects.get(pk=food_id)
        return render(request,'detail.html',{'food':food})
    
def update(request,food_id):
    food = Food.objects.get(pk=food_id)
    if request.method=="POST":
        form = PostModelForm(request.POST,instance=food)
        if form.is_valid():
            food = form.save()
            foods = Food.objects.filter(category=food.category)
            return redirect('post:detail', food.pk)
    else:
        form = PostModelForm(initial={'category':food.category})
    return render(request,'create.html',{'form':form,'category':food.category})
    
def delete(request,food_id):
    food = Food.objects.get(pk=food_id)
    category = food.category
    foods = Food.objects.filter(category=category)
    food.delete()
    return render(request,'list.html',{'foods':foods,'category':category})