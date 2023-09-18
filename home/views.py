from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
   return render(request,'home/home.html')
    
def about(request):
   return render(request,'home/about.html')

def sing_up(request):
   return render(request,'home/sing_up.html', {
                  'form' : UserCreationForm
   }) 
