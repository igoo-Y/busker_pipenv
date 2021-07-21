from django.db import models
from core import models as core_models
from users import models as user_models
from django_countries.fields import CountryField


class AbstractItem(core_models.TimeStampedModel):

    """Abstract Item Model Definition"""

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Genre(AbstractItem):

    """Genre Model Definition"""

    pass

    class Meta:
        verbose_name = "Genre"


class PictureQuality(AbstractItem):

    """Picture Quality Model Definition"""

    pass

    class Meta:
        verbose_name = "Picture Quality"


class Broadcast(core_models.TimeStampedModel):

    """Broadcast Model Definition"""

    name = models.CharField(max_length=120, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="broadcast_images", blank=True, null=True)
    on_air = models.BooleanField(default=False)
    country = CountryField(blank_label="(select country)", default="kr")
    genre = models.ManyToManyField("Genre", blank=True)
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

    def __str__(self):
        return self.name
