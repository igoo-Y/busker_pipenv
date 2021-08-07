from django.urls import path
from . import views

app_name = "broadcasts"

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:pk>/", views.get_random_on_air, name="random"),
    path("main", views.main_view, name="main"),
    path("<int:pk>/", views.BroadcastDetail.as_view(), name="detail"),
    path("create/", views.CreateBroadcastView.as_view(), name="create"),
    path("update/<int:pk>/", views.EditBroadcastView.as_view(), name="edit"),
]
