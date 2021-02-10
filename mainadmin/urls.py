from django.urls import path,include
from .views import *
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    
    path('',DashBoard.as_view(),name="dashboard"),
    path('category',AddCategory.as_view(),name="category"),
    path('product',AddProduct.as_view(),name="product"),
    path('editproduct/<int:id>',EditProduct.as_view(),name="editproduct"),
    path('deleteproduct/<int:id>',DeleteProduct.as_view(),name="deleteproduct"),
    path('fetchproduct/<int:id>',FetchProduct.as_view(),name="fetchproduct"),

    

    





    
]
