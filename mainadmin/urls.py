from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    
    path('',DashBoard.as_view(),name="dashboard"),
    path('category',AddCategory.as_view(),name="category"),
    path('product',AddProduct.as_view(),name="product"),

    





    
]
