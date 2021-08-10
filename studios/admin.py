from django.contrib import admin
from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    # Post Admin Definition

    list_display = [
        "title",
        "writer",
        "p_studio",
        "post_category",
    ]


@admin.register(models.Studio)
class StudioAdmin(admin.ModelAdmin):

    # Studio Admin Definition

    list_display = [
        "name",
        "studio_host",
        "count_posts",
    ]

    raw_id_fields = ("studio_host",)

    def count_posts(self, obj):
        return obj.posts.count()

    count_posts.short_description = "Number of Posts"
