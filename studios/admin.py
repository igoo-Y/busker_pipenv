from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):

    """Category Admin Definition"""

    pass


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    """Post Admin Definition"""

    pass


@admin.register(models.Studio)
class StudioAdmin(admin.ModelAdmin):

    """Studio Admin Definition"""

    list_display = [
        "name",
        "host",
    ]

    raw_id_fields = ("host",)
