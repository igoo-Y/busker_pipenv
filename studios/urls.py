from django.urls import path
from . import views

app_name = "studios"


urlpatterns = [
    path("create/", views.CreateStudioView.as_view(), name="create"),
    path("<int:pk>/", views.DetailStudioView.as_view(), name="detail"),
]
