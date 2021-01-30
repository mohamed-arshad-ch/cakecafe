from django.urls import path,include
from .views import *
urlpatterns = [
    
    path('',LandingPage.as_view(),name="landingpage")

    
]
