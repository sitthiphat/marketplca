from django.db import models
from mysite.models import *
from products.models import *
from django.utils import timezone
from django.contrib.auth.models import User, auth

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    total = models.FloatField(null=True)
    date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    ship = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)
    ship = models.BooleanField(default=False)
    
    
    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name
    


    
    