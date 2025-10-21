from django.urls import path
from . import views


urlpatterns = [
    path("home", views.return_warehouse_dashboard)
]