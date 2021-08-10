from django.db import models
from core import models as core_models
from users import models as user_models
from studios import models as studio_models


class Category(core_models.TimeStampedModel):

    """Category Model Definition"""

    NOTICE = "NT"
    BULLETIN = "BL"
    BOARD_CHOICES = [
        (NOTICE, "공지사항"),
        (BULLETIN, "자유게시판"),
    ]

    name = models.CharField(max_length=2, choices=BOARD_CHOICES, default=BULLETIN)

    def __str__(self):
        return self.name


class Post(core_models.TimeStampedModel):

    """Post Model Definition"""

    title = models.CharField(max_length=200, blank=True, null=True)
    writer = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    studio = models.ForeignKey(
        studio_models.Studio, related_name="posts", on_delete=models.CASCADE
    )
    category = models.CharField(max_length=40, null=True)

    def __str__(self):
        return self.title[:30]
