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
    path('addtocart/<int:id>',csrf_exempt(AddToCart.as_view()),name="addtocart"),
    path('cart',csrf_exempt(Cart.as_view()),name="cart"),
    path('checkout',csrf_exempt(Checkout.as_view()),name="checkout"),
    path('addpayment',csrf_exempt(AddPayment.as_view()),name="addpayment"),
    path('myorders',csrf_exempt(ViewMyOrder.as_view()),name="myorders"),
    path('deleteitemfromcart/<int:id>',csrf_exempt(DeleteItemFromCart.as_view()),name="deleteitemfromcart"),

    path('productdetails/addtocart/<int:id>',csrf_exempt(AddToCart.as_view()),name="addtocart"),
    path('cancelproduct/<int:id>',csrf_exempt(CancelProduct.as_view()),name="cancelproduct"),











    
]
