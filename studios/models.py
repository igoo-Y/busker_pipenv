from django.db import models
from core import models as core_models
from users import models as user_models


class StudioAbstractItem(core_models.TimeStampedModel):

    """Studio Abstract Item Model Definition"""

    name = models.CharField(max_length=120)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class PostCategory(StudioAbstractItem):

    """PostCategory Model Definition"""

    pass


class Post(core_models.TimeStampedModel):

    # Post Model Definition

    title = models.CharField(max_length=200, blank=True, null=True)
    writer = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    p_studio = models.ForeignKey(
        "Studio", related_name="posts", on_delete=models.CASCADE
    )
    post_category = models.ForeignKey(
        "PostCategory", related_name="posts", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title[:30]


class Studio(core_models.TimeStampedModel):

    # Studio Model Definition

    name = models.CharField(max_length=160, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="studio_images", blank=True, null=True)
    studio_host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
