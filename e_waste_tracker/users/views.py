from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def return_login_page(request):
    return render(request, "users/login.html")

def return_signup_page(request):
    return render(request, "users/signup.html")

def return_root_directory(request):
    return render(request, "users/main.html")
    