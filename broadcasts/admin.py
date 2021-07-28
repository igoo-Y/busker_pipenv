from core import models
from django.contrib import admin
from . import models


@admin.register(models.PictureQuality)
class PictureQualityAdmin(admin.ModelAdmin):

    """PictureQuality Admin Defintion"""

    pass


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):

    """Genre Admin Defintion"""

    pass


@admin.register(models.Broadcast)
class BroadcastsAdmin(admin.ModelAdmin):

    """Broadcast Admin Model"""

    list_display = [
        "name",
        "host",
        "country",
        "picture_quality",
        "on_air",
    ]

    list_filter = [
        "on_air",
    ]
