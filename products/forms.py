from django.forms import ModelForm
from .models import *

from django import forms

class ProductFormproduct(ModelForm):
    class Meta:
        model = Product
        fields = ('name','category','brand','gender','color','size','detail','image_url','instock','price')