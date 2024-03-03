from django import forms
from .models import Products


class Product(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"

from .models import ItemModel

class PaymentForm(forms.ModelForm):
    class Meta:
        model = ItemModel
        fields = ['name','amount']        
