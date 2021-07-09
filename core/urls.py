from django.urls import path
from broadcasts import views as broadcast_views

app_name = "core"

urlpatterns = [path("", broadcast_views.home, name="home")]
