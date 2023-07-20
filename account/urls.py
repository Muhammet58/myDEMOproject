from django.urls import path
from . import views


urlpatterns = [
    path("login", views.login_request, name="login_url"),
    path("register", views.register_request, name="register_url"),
    path("logout", views.logout_request, name="logout")
]