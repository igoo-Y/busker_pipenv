from django.urls import path
from . import views

app_name = "broadcasts"

urlpatterns = [
    path("", views.home, name="home"),
    path("main", views.main_view, name="main"),
    path("create/", views.CreateBroadcastView.as_view(), name="create"),
    path("<int:pk>/", views.BroadcastDetail.as_view(), name="detail"),
    path("update/<int:pk>/", views.UpdateBroadcastView.as_view(), name="update"),
]
