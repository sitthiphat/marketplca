
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import loader
from mysite.models import *
from .models import *
from django.contrib.auth.models import User, auth
from .forms import *
from django.contrib.auth.decorators import login_required
from cart.models import *
from cart.views import *
# Create your views here.


def shop(request,cat_id=None):
    cart = get_user_cart(request)
    category = None
    cartitem = CartItem.objects.filter(cart=cart)
    categories =Category.objects.all()
    
    products = Product.objects.filter(status=True).order_by('-id')
    if cat_id:
        category = get_object_or_404(Category,id=cat_id)
        products = products.filter(category=category)
    
    return render(request, 'product/shop.html', {'products':products,
                                                 'category':category,
                                                 'categories':categories,
                                                 'cartitem':cartitem})



def addproduct(request):
    formproduct = ProductFormproduct()
    if request.method == 'POST':
        formproduct = ProductFormproduct(request.POST, request.FILES) 
        if formproduct.is_valid():
            instance = formproduct.save(commit=False)
            instance.p_seller = request.user.seller
            instance.save()
            messages.success(request, 'เพิ่มข้อมูลสินค้าเรียบร้อยแล้ว')
            return redirect('user')
    context = {'formproduct':formproduct}
    return render(request, 'product/addproduct.html', context)



def productdetail(request, pk):
    productdetail1 = Product.objects.get(id=pk)
    context = {'productdetail':productdetail1} 
    return render(request, 'product/productdetail.html',context)

def editProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductFormproduct(instance=product)  
    if request.method == 'POST':
        form = ProductFormproduct(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,'แก้ไขข้อมูลเรียบร้อย')
            return redirect('user')
        
    context = {'formproduct':form}
    return render(request, 'product/addproduct.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, 'ลบสินค้าเรียบร้อยแล้ว')
        return redirect('user')
    context = {'product':product}
    return render(request, 'product/deleteproduct.html', context)