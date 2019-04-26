from django.shortcuts import render,redirect
from .models import Person
from .forms import PersonForm
from django.views.generic import ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# def list(request):
#     people = Person.objects.all()
#     return render(request,'person/person_list.html',{'people':people})

class PersonList(ListView):
    model = Person
    context_object_name = 'people'
    
# def create(request):
#     if request.method == 'GET':
#         form = PersonForm()
#         return render(request,'person/person_form.html',{'form':form})
#     else:
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         age = request.POST.get('age')
#         Person.objects.create(last_name=last_name,email=email,age=age)
#         return redirect('list')

class PersonCreate(LoginRequiredMixin,CreateView):
    model = Person
    form_class = PersonForm
    success_url = '/person/'