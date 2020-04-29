
from django.db import models
from django.contrib.auth import get_user_model
from products.models import *
from mysite.models import *
from order.models import *
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    date_added = models.DateField(auto_now_add=True)

   

    def __str__(self):
        return self.user.first_name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    

    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.product.name
    

class Paycart(models.Model):
    cartitem = models.ForeignKey(OrderItem,on_delete=models.CASCADE)
    simage_url = models.ImageField(blank=True,null=True)
    image_url = models.ImageField(blank=True,null=True)
    date = models.DateTimeField(default=timezone.now)
    payed = models.BooleanField(default=True)
    
    def __str__(self):
        return '%s จาก %s' %(self.cartitem.product.name,self.payed)
    
    
    