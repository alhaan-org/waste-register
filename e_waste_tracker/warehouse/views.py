from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
import json

from .forms import ItemForm
from .models import Item
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
        warehouse = getattr(request.user, 'warehouse_owner', None)
        if not warehouse:
            from django.contrib import messages
            messages.error(request, "Warehouse not configured for your account.")
            return redirect('warehouse:home')
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
            warehouse = getattr(request.user, 'warehouse_owner', None)
            if not warehouse:
                return JsonResponse({
                    "status": "error",
                    "message": "Warehouse not configured for your account."
                }, status=400)
            
            data = json.loads(request.body)
            parsed_data = parse_item_data(data)
            item = Item(
                **parsed_data,
                warehouse=warehouse
            )
            item.save()
            return JsonResponse({
                "status": "success",
                "message": "Item added successfully!",
                "data_received": data
            })

        except json.JSONDecodeError:
            return JsonResponse({
                "status": "error",
                "message": "Invalid JSON format"
            }, status=400)
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error in AddItemInItemView: {str(e)}")
            return JsonResponse({
                "status": "error",
                "message": "Server error. Please try again."
            }, status=500)

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