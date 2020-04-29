
from django.contrib import messages
from django.template import loader
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from products.models import Product
from .models import * 
from mysite.forms import *
from .forms import *
from order.models import *
from products.models import *
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def get_user_cart(request):
    """Retrieves the shopping cart for the current user."""
    cart_id = None
    cart = None
    # If the user is logged in, then grab the user's cart info.
    if request.user.is_authenticated and not request.user.is_anonymous:
        try:
            cart = Cart.objects.get(user=request.user)
        except Cart.DoesNotExist:
            cart = Cart(user=request.user)
            cart.save()
    
    
        
    return cart


def add_cart(request, product_id):
    cart = get_user_cart(request)
    product = Product.objects.get(id=product_id)
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.instock:
            cart_item.quantity += 1
            messages.info(request,'เพิ่มในตะกร้าแล้ว')
            
        else:
            messages.info(request,'สินค้ามีไม่เพียงพอ')
            
        cart_item.save()
        
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart
            )
        cart_item.save()
        messages.info(request,'เพิ่มในตะกร้าแล้ว')
    return redirect('product:shop')  

def cart_remove(request, product_id):
    cart = get_user_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        messages.info(request,'ลดจำนวน')
        cart_item.save()
    else:
        messages.info(request,'ไม่มีสินค้าในตะกร้า')
        cart_item.delete()
        return redirect('product:shop')
    return redirect('cart:cartdetail')  

def full_remove(request, product_id):
    cart = get_user_cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    messages.info(request,'ไม่มีสินค้าในตะกร้า')
    cart_item.delete()
    return redirect('product:shop')



def cart_detail(request, total=0, cart_items = None):
    try:
        cart = get_user_cart(request)
        cart_items = CartItem.objects.filter(cart=cart, active=False)
        
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            
    except ObjectDoesNotExist:
        pass
    cart_itemstrue = CartItem.objects.filter(cart=cart, active=True)
    context = {'cartitem':cart_items,'total':total,'cartitemtrue':cart_itemstrue}
    return render(request,'cart/cart.html',context)

def add_cartdetail(request, product_id):
    cart = get_user_cart(request)
    product = Product.objects.get(id=product_id)
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.instock:
            cart_item.quantity += 1
            messages.info(request,'เพิ่มจำนวน')
        else:
            messages.info(request,'สินค้ามีไม่เพียงพอ')
            
        cart_item.save()
        
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
                product = product,
                quantity = 1,
                cart = cart
            )
        cart_item.save()
    return redirect('cart:cartdetail')

def cart_detail1(request, total=0, cart_items = None):
    cart = get_user_cart(request)
    cart_items = CartItem.objects.filter(cart=cart, active=False)
      
    context = {'cartitem':cart_items}
    return render(request,'master.html',context)



def checkout(request,total=0):
    cart = get_user_cart(request)
    cart_items = CartItem.objects.filter(cart=cart, active=False)
    address = Address.objects.filter(user=request.user)
    for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)  
    context = {'cart':cart_items,'address':address,'total':total}
    return render(request, 'cart/checkout.html',context)


def paymentcart(request,cartitem_id):    
    seller = SellerBank.objects.all()
    orderitem = OrderItem.objects.get(id=cartitem_id)
    if request.method == 'POST':
        paycart = Paycart.objects.create(
            cartitem = orderitem,
            
            image_url = request.FILES.get('img')
            
            
        )
        paycart.save()
        
        orderitem.status = True
        orderitem.save()
        products = Product.objects.get(id=orderitem.product.id)
        products.instock = int(orderitem.product.instock - orderitem.quantity)
        if products.instock == 0 : 
            products.status = False
            products.save()
        else: 
            products.save()
        messages.info(request,'ชำระเงินเรียบร้อย') 
        return redirect('buyer')
    
    
    context = {'cartitem':orderitem,'sellerbank':seller}
    return render(request,'cart/payment.html',context)
    
    


def payment(request,total=0):
    try:
        cart = get_user_cart(request)
        cart_items = CartItem.objects.filter(cart=cart, active=False)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            
            
    except ObjectDoesNotExist:
        pass
    if request.method == 'GET':
        
        order = Order.objects.create(
            user = request.user,
            total = total
        )
        order.save()
            
        for item in cart_items:
            oi=OrderItem.objects.create(
                order = order,
                product = item.product,
                quantity = item.quantity,
                    
            )
            oi.save()
            
            item.delete()
            print('The order has been created')
            
        messages.info(request,'ยืนยันคำสั่งซื้อเรียบร้อย') 
        context = {'order': order}
        return redirect('buyer')
    
              
def orderview(request, order_id):
    order= Order.objects.get(id=order_id)
    orderitem = OrderItem.objects.filter(order=order_id)
    for i in orderitem:
        if i.status == True :
            i.order.status = True
            i.order.save()
        else :
            i.order.status = True
            i.order.save()
         
    context = {'orderitem':orderitem,'order':order}
    return render(request, 'cart/orderview.html',context)
     
def bill(request, order_id):
    order= Order.objects.get(id=order_id)
    orderitem = OrderItem.objects.filter(order=order_id)
    address = Address.objects.all()
    context = {'orderitem':orderitem,'order':order,'address':address}
    return render(request, 'payment/bill.html',context)
    
    
def sellerpayment(request, payment_id):
    paycart = Paycart.objects.get(id=payment_id) 
    address = Address.objects.all()
    if request.method =='POST':
        paycart.simage_url = request.FILES.get('img')
        paycart.save()
        messages.info(request,'ทำการจัดส่งเรียบร้อย')
        return redirect('user')
   
    context = {
               'paycart':paycart,
               'address':address
               }
    return render(request, 'payment/paymentseller.html',context)

