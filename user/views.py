from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import auth
from .models import *
from django.contrib.auth import authenticate
# Create your views here.


#Landing Page View
class LandingPage(View):
    
    #Render Landing PAge
    def get(self, request, *args, **kwargs):
        try:
            return render(request,'user/index.html')
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

# Login For User

class LoginPage(View):
    #Render Login PAge
    def get(self, request, *args, **kwargs):
        try:
            return render(request,'user/login.html')
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})
    
    #Post Login
    def post(self, request, *args, **kwargs):
        try:
            try:
                
                user = authenticate(username=request.POST['username'],password=request.POST['password'])
               
                if user is not None:
                    auth.login(request, user)
                    
                    return redirect('landingpage')
                else:
                    
                    return redirect('userlogin')
            except CustomUser.DoesNotExist:
                
                return redirect('userlogin')
                    
            
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})