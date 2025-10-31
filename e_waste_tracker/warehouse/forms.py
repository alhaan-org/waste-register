from django.forms import ModelForm
from django import forms
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['product_name', 'quantity', 'type', 'cost_price', 'sold_price', 'description', 'is_sold']
        widgets = {
            "product_name" : forms.TextInput(attrs={"class" : "form-control", "placeholder" : "Enter Product name"}),
            "quantity" : forms.NumberInput(attrs={"class": "form-control", "placeholder" : "No. of quantity"}),
            "type":  forms.Select(attrs={"class": "form-select"}),
            "cost_price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Cost Price"}),
            "sold_price": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Selling Price"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "is_sold" : forms.CheckboxInput(attrs={"class": "form-check-input"})
        }
