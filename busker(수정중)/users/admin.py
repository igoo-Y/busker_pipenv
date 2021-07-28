from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):

    """Custom User Admin"""

    list_display = [
        "username",
        "email",
        "nickname",
        "gender",
        "language",
        "currency",
        "busker",
    ]

    list_filter = UserAdmin.list_filter + ("busker",)

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "nickname",
                    "bio",
                    "gender",
                    "birthdate",
                    "phone",
                    "language",
                    "currency",
                    "busker",
                ),
            },
        ),
    )
