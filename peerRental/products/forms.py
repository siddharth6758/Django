from django import forms
from products.models import *

class ProductFrom(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_image','description','price','rent_type','title']