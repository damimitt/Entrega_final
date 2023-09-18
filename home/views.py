from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
   return render(request,'home/home.html')
    
def about(request):
   return render(request,'home/about.html')

def sign_up(request):
  
   if request.method == 'GET':
      print('Enviando datos a la pagina')   
      return render(request,'home/sign_up.html', { 
                  'form' : UserCreationForm
   })
   
   else:
      print(request.POST)
      if request.POST['password1'] == request.POST['password2']:
         try:
         #Registrar al usuario.
            user = User.objects.create_user(username= request.POST['username'], 
                                          password= request.POST['password1']
                                         )
            user.save()
            print('usuario registrado exitosamente')
            return redirect('home') 
         except:
            return HttpResponse('El usuario ya existe')
      else:
         return HttpResponse('Las contraseñas no coinciden')
