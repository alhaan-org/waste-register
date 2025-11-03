from django.urls import path
from . import views

# APP_NAME "Warehouse"
app_name = "warehouse"

urlpatterns = [
    # Template Views with Rendered Data
    path("home/", views.WareHouseView.as_view(), name="home"),
    path("home/status/", views.WareHouseStatus.as_view(), name="status"),
    path("home/checkinandout/", views.WareHouseCheckInOut.as_view(), name="checkinandout"),
    path("home/revenue/", views.WareHouseRevenueView.as_view(), name="revenue"),
    path("home/settings/", views.WareHouseSettingsView.as_view(), name="settings"),
    path("logout/", views.LogoutWareHouse.as_view(), name="logout"),

    # CRUD API Endpoints / AJAX Views
    path("api/add_item/", views.AddItemInItemView.as_view(), name="add_item"),
    path("api/update_item/<int:id>/", views.UpdateItemInItemView.as_view(), name="update_item"),
    path("api/delete_item/<int:id>/", views.DeleteItemInItemView.as_view(), name="delete_item"),

]

