from django.urls import path

# from .views import CreateStudioView, DetailStudioView
from . import views

app_name = "studios"


urlpatterns = [
    # path("", views.home, name="home"),
    path("create/", views.CreateStudioView.as_view(), name="create"),
    path("<int:pk>/", views.DetailStudioView.as_view(), name="detail"),
]

# views.CreateBroadcastView.as_view()
