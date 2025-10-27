from django.urls import path
from . import views

app_name = "warehouse"

urlpatterns = [
    path("home", views.WareHouseView.as_view(), name="home")
]