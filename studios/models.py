from typing import Tuple
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from core import models as core_models
import core
from users import models as user_models


class Category(core_models.TimeStampedModel):

    """Category Model Definition"""

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(core_models.TimeStampedModel):

    """Post Model Definition"""

    class Meta:
        ordering = ["-created"]

    NOTICE = "NT"
    BULLETIN = "BL"
    BOARD_CHOICES = [
        (NOTICE, "공지사항"),
        (BULLETIN, "자유게시판"),
    ]

    title = models.CharField(max_length=200, null=True)
    writer = models.ForeignKey(
        user_models.User, related_name="posts", on_delete=models.CASCADE
    )
    body = RichTextUploadingField(null=True)
    studio = models.ForeignKey("Studio", related_name="posts", on_delete=models.CASCADE)
    category = models.CharField(
        max_length=40, null=True, choices=BOARD_CHOICES, default=BULLETIN
    )

    def __str__(self):
        return self.title[:30]


class Studio(core_models.TimeStampedModel):

    """Studio Model Definition"""

    name = models.CharField(max_length=160, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="studio_images",
        blank=True,
        null=True,
        default="broadcast_images/no_image.png",
    )
    host = models.OneToOneField(
        user_models.User,
        related_name="studio",
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("studios:detail", kwargs={"pk": self.pk})
