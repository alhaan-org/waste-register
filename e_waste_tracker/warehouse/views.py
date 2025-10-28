from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

class WareHouseView(View):
    def get(self, request):
        return render(request, "warehouse/dashboard.html")

class WareHouseStatus(View):
    def get(self, request):
        return render(request, "warehouse/status.html")

class WareHouseCheckInOut(View):
    def get(self, request):
        return render(request, "warehouse/checkinout.html")

class WareHouseRevenueView(View):
    def get(self, request):
        return render(request, "warehouse/revenue.html")

class WareHouseSettingsView(View):
    def get(self, request):
        return render(request, "warehouse/settings.html")