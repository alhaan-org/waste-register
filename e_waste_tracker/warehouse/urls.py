from django.urls import path
from . import views

app_name = "warehouse"

urlpatterns = [
    path("home/", views.WareHouseView.as_view(), name="home"),
    path("home/status/", views.WareHouseStatus.as_view(), name="status"),
    path("home/checkinout/", views.WareHouseCheckInOut.as_view(), name="checkinout"),
    path("home/revenue/", views.WareHouseRevenueView.as_view(), name="revenue"),
    path("home/settings/", views.WareHouseSettingsView.as_view(), name="settings")
]