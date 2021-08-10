from django.urls import path
from . import views

app_name = "broadcasts"

urlpatterns = [
    path("", views.home, name="home"),
    path("main", views.main_view, name="main"),
    path("<int:pk>/", views.BroadcastDetail.as_view(), name="detail"),
    path("create/", views.CreateBroadcastView.as_view(), name="create"),
    path("update/<int:pk>/", views.UpdateBroadcastView.as_view(), name="update"),
]
