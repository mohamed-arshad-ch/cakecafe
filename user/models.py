from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    calling_code = models.CharField(max_length=100,null=True,blank=True)
    phone_number = models.CharField(max_length=100,null=True,blank=True)
    remember_me = models.BooleanField(default=True)
    


    def __str__(self):
        return self.username