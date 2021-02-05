from django.db import models
from django.contrib.auth.models import AbstractUser
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
        return self.title