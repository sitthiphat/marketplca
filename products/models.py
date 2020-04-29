from django.db import models
from mysite.models import Gender,Seller
from django.contrib.auth.models import User, auth
from django.utils import timezone
from django.urls import reverse
from mysite.models import *

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('product:category',
                       args=[self.id])

class Brand(models.Model):
    title = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class Color(models.Model):
    title = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class Size(models.Model):
    title = models.CharField(max_length=300)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender,null=True, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    p_seller = models.ForeignKey(Seller,null=True, on_delete=models.SET_NULL)
    detail = models.TextField(max_length=1000)
    image_url= models.ImageField(null=True, blank=True)
    instock = models.PositiveIntegerField(default=1)
    price = models.FloatField(default=1)
    status = models.BooleanField(default=True)    
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return '%s จาก %s' %(self.name,self.p_seller)
    
    
class Productsaled(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    
    
    date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.product.name
    
    

