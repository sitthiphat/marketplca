from django.forms import ModelForm
from .models import *

from django import forms

class Addressform(ModelForm):
    class Meta:
        model = Address
        fields = ['number','country','city','tumbon','zipcode']
        
class Bankform(ModelForm):
    class Meta:
        model = SellerBank
        fields = ['bank','namebank','number']