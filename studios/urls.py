from django.urls import path
from . import views

app_name = "studios"

<<<<<<< HEAD

urlpatterns = [
    path("create/", views.CreateStudioView.as_view(), name="create"),
    path("<int:pk>/", views.DetailStudioView.as_view(), name="detail"),
=======
urlpatterns = [
    path("create/", views.CreateStudioView.as_view(), name="create"),
    path("<int:pk>/", views.DetailStudioView.as_view(), name="detail"),
    path("update/<int:pk>/", views.UpdateStudioView.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeleteStudioView.as_view(), name="delete"),
>>>>>>> ingyu
]
