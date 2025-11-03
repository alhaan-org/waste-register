from django.forms import ModelForm
from django import forms
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['product_name', 'quantity', 'type', 'cost_price', 'sold_price', 'description', 'is_sold']
        widgets = {
            "product_name" : forms.TextInput(attrs={"id":"product-name", "class" : "form-control", "placeholder" : "Enter Product name"}),
            "quantity" : forms.NumberInput(attrs={"id":"quantity","class": "form-control", "placeholder" : "No. of quantity"}),
            "type":  forms.Select(attrs={"id":"type","class": "form-select"}),
            "cost_price": forms.NumberInput(attrs={"id":"cost_price","class": "form-control", "placeholder": "Cost Price"}),
            "sold_price": forms.NumberInput(attrs={"id":"sold_price","class": "form-control", "placeholder": "Selling Price"}),
            "description": forms.Textarea(attrs={"id":"desc","class": "form-control"}),
            "is_sold" : forms.CheckboxInput(attrs={"id":"is_sold","class": "form-check-input"})
        }
