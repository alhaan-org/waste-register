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
            return redirect("warehouse:status")
        else:
            messages.error(request, "Authentication failed")
    return render(request, "users/login.html")

def return_signup_page(request):
    form = CreateUserWithCredentials()
    if request.method == 'POST':
        form = CreateUserWithCredentials(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, "✓ Signup Successful! Please login with your credentials.")
                return redirect("login")
            except Exception as e:
                messages.error(request, f"Error creating account: {str(e)}")
                form.add_error(None, "An unexpected error occurred. Please try again.")
                
    context = {"form": form}
    return render(request, "users/signup.html", context)

def return_root_directory(request):
    return render(request, "users/main.html")
    