from django.urls import path
from . import views

app_name = "broadcasts"

urlpatterns = [
    path("", views.home, name="home"),
    path("main", views.main_view, name="main"),
    path("<str:pk>/", views.broadcast_detail, name="detail"),
    path("create/", views.CreateBroadcastView.as_view(), name="create"),
]
