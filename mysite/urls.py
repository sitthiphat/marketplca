from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('logout', views.Logout, name="logout"),
    path('user', views.user, name="user"),
    path('buyer', views.buyer, name="buyer"),
    path('userprofile/<int:id>/', views.sellerprofile,name='sellerprofile'),
    path('adduser/<int:id>/', views.adduser, name="adduser"),
    path('addbuyer/<int:id>/', views.addbuyer, name="addbuyer"),
    path('addaddress', views.addaddress, name="addaddress"),
    path('editaddress/<int:id>/', views.editAddress, name="editaddress"),
    path('addbank', views.addbank, name="addbank"),
]