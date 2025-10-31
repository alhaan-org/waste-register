from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ItemForm
from .models import Warehouse, Item
# Create your views here.

@method_decorator(login_required(login_url="login"), name="dispatch")
class WareHouseView(View):
    def get(self, request):
        user = request.user
        context = {"user": user}
        return render(request, "warehouse/dashboard.html")

@method_decorator(login_required(login_url="login"), name="dispatch")
class WareHouseStatus(View):
    def get(self, request):
        user = request.user
        context = {"user": user}
        return render(request, "warehouse/status.html", context)

@method_decorator(login_required(login_url="login"), name="dispatch")
class WareHouseCheckInOut(View):
    def get(self, request):
        warehouse = request.user.warehouse_owner
        items = warehouse.items.all()
        form = ItemForm()
        context = {"items": items, "form": form}
        return render(request, "warehouse/checkinandout.html", context)

    # This code is for testing, This will be removed since it is causing bugs,
    # The only way to resolve is to make AJAX Views for CRUD operations
    # def post(self, request):
    #     warehouse = request.user.warehouse_owner
    #     action = request.POST.get('action')
    #     form = ItemForm(request.POST)
    #
    #     if action == "add":
    #         if form.is_valid():
    #             new_item = form.save(commit=False)
    #             new_item.warehouse = warehouse
    #             new_item.save()
    #     elif action == "update":
    #         item_id = request.POST.get("item_id")  # you need a hidden input for item_id
    #         item = Item.objects.get(pk=item_id, warehouse=warehouse)
    #         for field, value in form.cleaned_data.items():
    #             setattr(item, field, value)
    #         item.save()
    #     elif action == "delete":
    #         item_id = request.POST.get("item_id")
    #         Item.objects.filter(pk=item_id, warehouse=warehouse).delete()
    #     elif action == "checkin":
    #         item_id = request.POST.get("item_id")
    #         item = Item.objects.get(pk=item_id, warehouse=warehouse)
    #         item.is_sold = False
    #         item.save()
    #     elif action == "checkout":
    #         item_id = request.POST.get("item_id")
    #         item = Item.objects.get(pk=item_id, warehouse=warehouse)
    #         item.is_sold = True
    #         item.save()
    #
    #     return redirect('warehouse:checkinandout')


@method_decorator(login_required(login_url="login"), name="dispatch")
class WareHouseRevenueView(View):
    def get(self, request):
        return render(request, "warehouse/revenue.html")

@method_decorator(login_required(login_url="login"), name="dispatch")
class WareHouseSettingsView(View):
    def get(self, request):
        return render(request, "warehouse/settings.html")


class LogoutWareHouse(View):
    def get(self, request):
        logout(request)
        return redirect("login")


class AddItemInItemView(View):
    pass

class UpdateItemInItemView(View):
    pass

class DeleteItemInItemView(View):
    pass

class MarkCheckInItemView(View):
    pass

class MarkCheckOutInItemView(View):
    pass