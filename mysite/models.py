from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, auth
# Create your models here.
class Gender(models.Model):
       name = models.CharField(max_length = 255, null=True)
       def __str__(self):
           return self.name

    

class Country(models.Model):
    name = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.name


    
    

class Address(models.Model):
    user = models.ForeignKey(User,null=True, on_delete=models.SET_NULL)
    number = models.TextField(null=True)
    tumbon  = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=255,null=True)
    country = models.ForeignKey(Country,null=True, on_delete=models.SET_NULL)
  
    zipcode = models.IntegerField(null=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.user.first_name
    
    
    
    #########################################################
    

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    address = models.TextField()
    image_url = models.ImageField(blank=True,null=True)
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name
    
    
class Bank(models.Model):
    name = models.CharField(max_length=255)
    image_url = models.ImageField(null=True,blank=True)
    careate = models.DateTimeField(timezone.now)
    
    def __str__(self):
        return self.name
    
class SellerBank(models.Model):
    user = models.ForeignKey(Seller, on_delete=models.CASCADE)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)
    namebank = models.CharField(max_length=255,null=True)
    number = models.IntegerField(null=True)
    create = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.bank.name
    
    
    
    

    
##############################################################################################################
    
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    image_url = models.ImageField(blank=True)
    
    def __str__(self):
        return self.user.first_name