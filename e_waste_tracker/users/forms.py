from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class CreateUserWithCredentials(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "phone", "cnic_no", "password1", "password2"]
        widgets = {
            "username": forms.TextInput(attrs={"id":"username", "class": "form-control", "placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"id": "email", "class": "form-control", "placeholder": "youremail@example.com"}),
            "phone": forms.TextInput(attrs={"id":"phone", "class": "form-control", "placeholder": "03xx-xxxxxxx"}),
            "cnic_no": forms.TextInput(attrs={"id":"id-card", "class": "form-control", "placeholder": "CNIC with Dashes"}),
            "password1": forms.PasswordInput(attrs={"id":"password", "class": "form-control", "placeholder": "Enter password"}),
            "password2": forms.PasswordInput(attrs={"id":"confirmPassword", "class": "form-control", "placeholder": "Confirm Password"})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'id': 'password',
            'placeholder': 'Enter Password',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'id': 'confirmPassword',
            'placeholder': 'Confirm Password',
        })



