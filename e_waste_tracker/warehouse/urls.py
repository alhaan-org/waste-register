from django.urls import path
from . import views

app_name = "warehouse"

urlpatterns = [
    path("home/", views.WareHouseView.as_view(), name="home"),
    path("home/status/", views.WareHouseStatus.as_view(), name="status"),
    path("home/checkinandout/", views.WareHouseCheckInOut.as_view(), name="checkinandout"),
    path("home/revenue/", views.WareHouseRevenueView.as_view(), name="revenue"),
    path("home/settings/", views.WareHouseSettingsView.as_view(), name="settings"),
    path("logout/", views.LogoutWareHouse.as_view(), name="logout")
]

