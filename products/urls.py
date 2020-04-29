from django.urls import path, include
from . import views

app_name ='product'
urlpatterns = [
    path('', views.shop, name="shop"),
    path('productdetail/<str:pk>/',views.productdetail,name='productdetail'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('edit_product/<str:pk>/',views.editProduct, name="edit_product"),
    path('delete_product/<str:pk>/',views.deleteProduct, name="delete_product"),
    path('caategory/<str:cat_id>/',views.shop, name="category"),
    
    
    
     ]