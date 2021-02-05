from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import auth
from .models import *
from django.contrib.auth import authenticate
import uuid
from django.core.mail import send_mail
# Create your views here.


#Landing Page View
class LandingPage(View):
    
    #Render Landing PAge
    def get(self, request, *args, **kwargs):
        try:
            
            product = Products.objects.all()
            index = {
                "products":product
            }
            return render(request,'user/index.html',index)
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


#Signup For User

class SignupPage(View):
    #render Signup Page
    def get(self, request, *args, **kwargs):
        try:
            return render(request,'user/register.html')
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

    # Register Post
    def post(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.create(username=request.POST['username'],first_name=request.POST['firstname'],last_name=request.POST['lastname'],phone_number=request.POST['username'],email=request.POST['email'],otp=str(uuid.uuid4())[:6],auth_key=str(uuid.uuid4()))
            user.set_password(request.POST['password'])
            user.save()

            userlogin = authenticate(username=request.POST['username'],password=request.POST['password'])

            if user is not None:
                auth.login(request, userlogin)
                    
                return redirect('landingpage')
            else:
                    
                return redirect('userlogin')

        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})        

class ResetPassword(View):
    def get(self, request):
        try:
            return render(request,'user/forgot-password.html')
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

    def post(self,request):
        try:
            email = request.POST['email']
            HOSTNAME = request.META['HTTP_HOST']
            otps = str(uuid.uuid4())[:6]
            user = CustomUser.objects.get(email=email)
            user.otp = otps
            user.auth_key = str(uuid.uuid4())
            user.save()
            email_url = 'http://'+str(HOSTNAME)+'/verification?auth='+user.auth_key
            email_msg = "<p>verification Code Is </p><br><h1>"+ user.otp +"</h1><a href='"+email_url+"'><button>Verify</button></a>"
            print(email_msg)
            email_res = send_mail('Otp Verification', 'The Otp is  '+user.otp, 'mohamedarshadcholasseri5050@gmail.com',[email], fail_silently=False,html_message=email_msg)

            return render(request,'user/mail-send.html')
        except CustomUser.DoesNotExist:
            return redirect("resetpassword")
        
            
class VerifyEmail(View):
    def get (self,request):
        try:
            return render(request,'user/verification-email.html')
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

    def post(self, request):
        
        
        code = request.POST['code']
        password = request.POST['password']

        try:
            user = CustomUser.objects.get(otp=code,auth_key=request.GET.get('auth', ''))
            user.otp = str(uuid.uuid4())[:6]
            user.auth_key = str(uuid.uuid4())
            user.set_password(password)
            user.save()
            return redirect("userlogin")

        except CustomUser.DoesNotExist:
            return redirect("resetpassword")

    