from django.urls import path
<<<<<<< HEAD

# from .views import CreateStudioView, DetailStudioView
=======
>>>>>>> ingyu
from . import views

app_name = "studios"

<<<<<<< HEAD

urlpatterns = [
    # path("", views.home, name="home"),
    path("create/", views.CreateStudioView.as_view(), name="create"),
    path("<int:pk>/", views.DetailStudioView.as_view(), name="detail"),
]

# views.CreateBroadcastView.as_view()
=======
urlpatterns = [
    path("create/", views.CreateStudioView.as_view(), name="create"),
    path("<int:pk>/", views.DetailStudioView.as_view(), name="detail"),
    path("update/<int:pk>/", views.UpdateStudioView.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeleteStudioView.as_view(), name="delete"),
]
>>>>>>> ingyu
