from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    
    path('',LandingPage.as_view(),name="landingpage"),
    path('login',csrf_exempt(LoginPage.as_view()),name="userlogin"),
    path('signup',csrf_exempt(SignupPage.as_view()),name="userregister"),
    path('forgotpassword',csrf_exempt(ResetPassword.as_view()),name="resetpassword"),
    path('verification',csrf_exempt(VerifyEmail.as_view()),name="verifyemail"),
    path('productdetails/<int:id>',csrf_exempt(ProductDetails.as_view()),name="productdetails"),






    
]
