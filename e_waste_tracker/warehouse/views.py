from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def return_warehouse_dashboard(request):
    return HttpResponse("Warehouse Dashboard Page")