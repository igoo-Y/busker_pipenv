from django.urls import path
from . import views

app_name = "studios"

urlpatterns = [
    path("create/", views.CreateStudioView.as_view(), name="create"),
    path("<int:pk>/", views.DetailStudioView.as_view(), name="detail"),
    path("update/<int:pk>/", views.UpdateStudioView.as_view(), name="update"),
    path("delete/<int:pk>/", views.DeleteStudioView.as_view(), name="delete"),
    path("<int:pk>/posts/", views.StudioPostsView.as_view(), name="posts"),
    path(
        "<int:pk>/posts/add",
        views.AddPostView.as_view(),
        name="add-post",
    ),
    path(
        "<int:studio_pk>/posts/<int:pk>/",
        views.DetailPostView.as_view(),
        name="post-detail",
    ),
]
