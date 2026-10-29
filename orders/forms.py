from django import forms
from .models import Order
class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        exclude = ['product']
        # fields='__all__'