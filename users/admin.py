from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

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

    list_filter = UserAdmin.list_filter + ("busker",)

    list_display = (
        "username",
        "email",
        "nickname",
        "gender",
        "language",
        "currency",
        "busker",
        "login_method",
    )
