from django import forms
from django.forms import ModelForm

from .models import *

class PaycartForm(ModelForm):
    class Meta:
        model = Paycart
        fields = ('image_url',)