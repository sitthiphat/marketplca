from django.urls import path, include
from . import views

app_name ='cart'
urlpatterns = [
    path('addcart/<int:product_id>/', views.add_cart,name='addcart'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),\
    path('full_remove/<int:product_id>/', views.full_remove, name='full_remove'),
    path('addcartd/<int:product_id>/', views.add_cartdetail,name='addcartdetail'),
    path('', views.cart_detail, name="cartdetail"),
    path('checkout', views.checkout, name="checkout"),
    path('payment', views.payment, name="payment"),
    path('paymentcart/<int:cartitem_id>/', views.paymentcart,name='paymentcart'),
    path('orderview/<int:order_id>/', views.orderview,name='orderview'),
    
    path('bill/<int:order_id>/', views.bill,name='bill'),
    path('payment/<int:payment_id>/', views.sellerpayment,name='sellerpayment'),
    path('del_order/<int:oi_id>/', views.del_order,name='del_order'),
    
    
    ]