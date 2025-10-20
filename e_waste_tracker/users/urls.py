from django.urls import path
from . import views

# Url Patterns 

urlpatterns = [
    path("", views.return_root_directory, name="root"),
    path("login", views.return_login_page, name="login")
]
