from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def return_login_page(request):
    return render(request, "users/main.html")

def return_root_directory(request):
    return HttpResponse("Server is running on Port 8000!")