from django.shortcuts import render,redirect
from django.http import JsonResponse
from .controller import *
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
            if request.user.is_authenticated:
                cartcount = Controller.CartCount(self,request.user)
                index = {
                    "products":product,
                    "cartcount":cartcount
                }
            
                return render(request,'user/index.html',index)
            else:
                index = {
                    "products":product,
                    "cartcount":0
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

class ProductDetails(View):
    def get (self,request,id):
        try:
            
            product = Products.objects.get(id=id)
            if request.user.is_authenticated:

                cartcount = Controller.CartCount(self,request.user)
                index = {
                    "products":product,
                    "cartcount":cartcount
                }
                return render(request,'user/product-details.html',index)
            else:
                cartcount = Controller.CartCount(self,request.user)
                index = {
                    "products":product,
                    "cartcount":0
                }
                return render(request,'user/product-details.html',index)
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class AddToCart(View):
    def get(self, request,id):
        try:
            if request.user.is_authenticated:
                
                product = Products.objects.get(id=id)
                try:
                    order = Order.objects.get(customer=request.user,status=False)
                    orderitem, created = OrderItem.objects.get_or_create(order=order,product=product)
                    orderitem.qty = orderitem.qty + 1
                    orderitem.save()
                    cartcount = Controller.CartCount(self,request.user)
                    return JsonResponse({"message":str(orderitem.qty),"cartcount":cartcount})
                except Order.DoesNotExist:
                    order = Order.objects.create(customer=request.user)
                    orderitem, created = OrderItem.objects.get_or_create(order=order,product=product)
                    orderitem.qty = orderitem.qty + 1
                    orderitem.save()
                    cartcount = Controller.CartCount(self,request.user)
                    return JsonResponse({"message":"Cart Added Successfully","carcount":cartcount})
            else:
                return JsonResponse({"message":"Please Login"})
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})


class Cart(View):
    def get (self,request):
        try:
            if request.user.is_authenticated:

                orderitems = OrderItem.objects.filter(order__customer=request.user,order__status=False)
                cartcount = Controller.CartCount(self,request.user)
                totalamount, totalpayamount = Controller.TotalAmount(self,request.user)
                index = {
                    "orderitem":orderitems,
                    "cartcount":cartcount,
                    "totalamount":totalamount
                }
                return render(request,'user/cart.html',index)
            else:
                index = {
                    
                    "cartcount":0,
                    
                }
                return render(request,'user/cart.html',index)

        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class Checkout(View):
    def get (self,request):
        try:
            if request.user.is_authenticated:

                orderitems = OrderItem.objects.filter(order__customer=request.user,order__status=False)
                cartcount = Controller.CartCount(self,request.user)
                totalamount,totalpayamount = Controller.TotalAmount(self,request.user)
                index = {
                    "orderitem":orderitems,
                    "cartcount":cartcount,
                    "totalamount":totalamount,
                    "totalpayamount":totalpayamount
                }
                return render(request,'user/checkout.html',index)
            else:
                return redirect("userlogin")
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class AddPayment(View):
    def post(self,request):
        try:
            try:
                order = Order.objects.get(customer=request.user,status=False)
                ShippingAddress.objects.create(status=True,order=order,address1=request.POST['address1'],address2=request.POST['address2'],city=request.POST['city'],state=request.POST['state'],zipcode=request.POST['zipcode'],payment_id=request.POST['paymentid'],amount=request.POST['amount'])
                order.status = True
                order.save()
                return JsonResponse({"message":"Success Your Payment"})
            except Order.DoesNotExist:
                return JsonResponse({"message":"Technical Issue"})
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})


class DeleteItemFromCart(View):
    def get(self,request,id):
        try:
            orderitem = OrderItem.objects.get(id=id).delete()
            return redirect("cart")
                
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})


class ViewMyOrder(View):
    def get(self,request):
        try:
            orderitems = OrderItem.objects.filter(order__customer=request.user)
            return render(request,"admin/view-my-orders.html",{"orderitems":orderitems})
                
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})

class CancelProduct(View):
    def get(self,request,id):
        try:
            orderitem = OrderItem.objects.get(id=id)
            orderitem.track = 3
            orderitem.save()
            return redirect("myorders")
        except Exception as e:
            print(e)
            return render(request,'user/404.html',{'mainerror':e})
