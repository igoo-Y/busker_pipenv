from django.db import models
from django.urls import reverse
from core import models as core_models
from users import models as user_models
from django_countries.fields import CountryField
import random
from random import randint
from django.db.models import Max


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item Model Definition"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PictureQuality(AbstractItem):

    """Picture Quality Model Definition"""

    pass

    class Meta:
        verbose_name = "Picture Quality"


class Genre(core_models.TimeStampedModel):

    """Genre Model Definition"""

    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to="genre_images", blank=True, null=True)

    class Meta:
        verbose_name = "Genre"

    def __str__(self):
        return self.name


class Broadcast(core_models.TimeStampedModel):

    """Broadcast Model Definition"""

    name = models.CharField(max_length=120, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to="broadcast_images",
        blank=True,
        null=True,
        default="broadcast_images/no_image.png",
    )
    on_air = models.BooleanField(default=False)
    country = CountryField(blank_label="(select country)", default="South Korea")
    genres = models.ManyToManyField("Genre", blank=True)
    picture_quality = models.ForeignKey(
        "PictureQuality", on_delete=models.SET_NULL, null=True, blank=True
    )
    host = models.ForeignKey(
        user_models.User,
        related_name="broadcasts",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def get_absolute_url(self):
        return reverse("broadcasts:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

    def get_on_airs(self):
        on_airs = Broadcast.objects.filter(on_air=True)
        return on_airs

    def get_random_pk(self):
        random_broadcast = Broadcast.objects.filter(on_air=True).order_by("?").first()
        random_pk = random_broadcast.pk
        return random_pk
