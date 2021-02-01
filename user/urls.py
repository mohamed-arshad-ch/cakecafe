from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    
    path('',LandingPage.as_view(),name="landingpage"),
    path('login',csrf_exempt(LoginPage.as_view()),name="userlogin"),
    path('signup',csrf_exempt(SignupPage.as_view()),name="userregister"),



    
]
