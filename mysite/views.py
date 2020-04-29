from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.template import loader
from . import models
from products.models import *
from django.contrib.auth.models import User, auth
from order.models import *
from cart.models import *
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
def index(request):
    return render(request, 'index.html')
    
  

def signup(request):
    
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['confirmpassword']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username ของท่านมีผู้ใช้งานแล้ว')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
               messages.info(request,'Email ของท่านมีผู้ใช้งานแล้ว')
               return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('user created')
                return redirect('signin')
        else:
            messages.info(request,'password ไม่ตรงกัน')
            return redirect('signup')
        return redirect('product:shop')

    else:
        return render(request, 'mysite/signup.html')   
    
    
def signin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'เข้าสู่ระบบเรียบร้อย')
            return redirect('product:shop')
        else:
            messages.success(request, 'เข้าสู่ระบบไม่สำเร็จ')
            return redirect('signin')
    else:
        
        return render(request, 'mysite/signin.html')    
    
def Logout(request):
    auth.logout(request)
    messages.success(request, 'คุณได้ออกจากระบบแล้ว')
    return redirect('signin')
########################################################################################################

def buyer(request):
    address = Address.objects.filter(user=request.user).order_by('-id')
    order = Order.objects.filter(user=request.user).order_by('-id')
    
    context = {'address':address,'order_items':order}
    return render(request, 'buyer/buyer.html',context)

 

def addbuyer(request, id):
    
    if request.method == 'POST':
        
        buyer = get_object_or_404(Buyer,user=id)
        user = get_object_or_404(User,id=id)
        user.first_name = request.POST['name']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.save()
        buyer.phone = request.POST['phone']
        buyer.image_url = request.FILES.get('img', buyer.image_url)
        buyer.save()
        messages.success(request, 'แก้ไขข้อมูลส่วนตัวเรียบร้อยแล้ว')
        return redirect('buyer')
    else:
        return render(request, 'buyer/addbuyer.html')

def addaddress(request):
    
    formaddress = Addressform()
    if request.method == 'POST':
        formaddress = Addressform(request.POST) 
        if formaddress.is_valid():
            instance = formaddress.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, 'เพิ่มข้อมูลที่อยู่เรียบร้อยแล้ว')
            return redirect('buyer')
    context = {'formaddress':formaddress}
    return render(request, 'buyer/addaddress.html', context)

def editAddress(request, id):
    address = Address.objects.get(id=id)
    form = Addressform(instance=address)  
    if request.method == 'POST':
        form = Addressform(request.POST,request.FILES, instance=address)
        if form.is_valid():
            messages.success(request,'แก้ไขข้อมูลที่อยู่เรียบร้อย')
            form.save()
            return redirect('buyer')
        
    context = {'formaddress':form}
    return render(request, 'buyer/addaddress.html', context)


####################################################################seller##############################

def user(request):    
    product = Product.objects.all().order_by('-id')
    orderitem = OrderItem.objects.all().order_by('-id')
    paycart = Paycart.objects.all()
    bank = SellerBank.objects.filter(user=request.user.seller).order_by('-id')
    
    context={
        'product':product,
        'orderitem':orderitem,
        'bank':bank,
        'paycart':paycart
        
    }
    return render(request, 'seller/user.html',context)


def adduser(request,id):
    if request.method =='POST':
        user = get_object_or_404(Seller,id=id)
        user.name = request.POST['name']
        user.email = request.POST['email'] 
        user.address = request.POST['address']
        user.image_url = request.FILES.get('img', user.image_url)
        user.save() 
        return redirect('user')  
    else:
        return render(request, 'seller/adduser.html')
    
    
    
    
    
    
    
    
    
    
def adduser3(request,id):
    seller = Seller.objects.get(id=id)
    if request.method == 'POST'and 'FILES':
        seller.name = request.POST['name']
        seller.email = request.POST['email']
        
        seller.address = request.POST['address']
        seller.image_url = request.FILES.get('img', seller.image_url)
        seller.save()
        
        return redirect('user')
    else:
        return render(request,'/adduser.html')
    




def sellerprofile(request, id):
    seller1 = Seller.objects.get(id=id)
    product = Product.objects.all().filter(p_seller=id)
    context = {'sellerprofile':seller1,
               'product':product
               }
    return render(request,'seller/userprofile.html' ,context)