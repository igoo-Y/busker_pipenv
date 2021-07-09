from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("users/login", views.LoginView.as_view(), name="login"),
    path("users/logout", views.log_out, name="logout"),
    path("users/signup", views.SignUpView.as_view(), name="signup"),
]
