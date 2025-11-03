from idlelib.debugobj import dispatch

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
import json

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

@method_decorator(csrf_exempt, name="dispatch")
class AddItemInItemView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            parsed_data = parse_item_data(data)
            print(request.user.warehouse_owner)
            item = Item(
                **parsed_data,
                warehouse=request.user.warehouse_owner
            )
            item.save()
            return JsonResponse({
                "status": "success",
                "message": "Item added successfully!",
                "data_received": data
            })

        except Exception as e:
            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=400)

class UpdateItemInItemView(View):
    pass

class DeleteItemInItemView(View):
    pass

def parse_item_data(data):
    def to_float(val):
        try:
            return float(val)
        except (ValueError, TypeError):
            return 0.0

    def to_int(val):
        try:
            return int(val)
        except (ValueError, TypeError):
            return 0

    return {
        "product_name": data.get("product_name", "").strip(),
        "quantity": to_int(data.get("quantity")),
        "type": data.get("type", "").strip(),
        "cost_price": to_float(data.get("cost_price")),
        "sold_price": to_float(data.get("sold_price")),
        "description": data.get("description", "").strip(),
        "is_sold": data.get("is_sold") == "on",
    }