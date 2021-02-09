from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.

class CustomUser(AbstractUser):
    calling_code = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=100,null=True,blank=True)
    remember_me = models.BooleanField(default=True)
    otp = models.CharField(max_length=100,null=True,blank=True)
    auth_key = models.CharField(max_length=100,null=True,blank=True)

    


    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.title

class Products(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100,null=True,blank=True)
    price = models.CharField(max_length=100,null=True,blank=True)
    stock = models.CharField(max_length=100,null=True,blank=True)
    weight = models.CharField(max_length=100,null=True,blank=True)

    
    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.CharField(max_length=100,default=str(uuid.uuid4())[:8])
    customer = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    track = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    track = models.IntegerField(default=0)
    qty = models.IntegerField(default=1)

    def subTotal(self):
        total = 0
        total = int(self.product.price) * self.qty
        return total
    def __str__(self):
        return self.order.order_id

class ShippingAddress(models.Model):
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    status = models.BooleanField()
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    amount = models.CharField(max_length=50)

    def __str__(self):
        return self.payment_id
