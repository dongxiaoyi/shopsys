#_*_coding:utf-8_*_
__author__ = 'dong'
from django import forms
from .models import Product
class ProductAdminForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = []
    def clean_price(self):
        if self.cleaned_data['price'] <= 0:
            raise forms.ValidationError("The price must biggist than 0")
        return self.cleaned_data['price']