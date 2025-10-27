from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserWithCredentials
from .models import CustomUser

# Create your views here.
def return_login_page(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user_obj = CustomUser.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except CustomUser.DoesNotExist:
            user = None
        
        if user is not None:
            login(request, user)
            return redirect("warehouse:home")
        else:
            messages.info(request, "Authentication failed")
    return render(request, "users/login.html")

def return_signup_page(request):
    form = CreateUserWithCredentials()
    if request.method == 'POST':
        
        form = CreateUserWithCredentials(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Signup Successfull")
            return redirect("login")
        else:
            return messages.info(request, "Wrong username or password")
    context = {"form": form}
    return render(request, "users/signup.html", context)

def return_root_directory(request):
    return render(request, "users/main.html")
    