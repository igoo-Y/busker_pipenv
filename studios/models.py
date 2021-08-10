from typing import Tuple
from django.db import models
from django.urls import reverse
from core import models as core_models
import core
from users import models as user_models


class Studio(core_models.TimeStampedModel):

    """Studio Model Definition"""

    name = models.CharField(max_length=160, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="studio_images",
        blank=True,
        null=True,
        default="studio_images/live_app_image.jpg",
    )
    host = models.OneToOneField(
        user_models.User, on_delete=models.CASCADE, primary_key=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("studios:detail", kwargs={"pk": self.pk})
