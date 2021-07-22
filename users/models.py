from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"
    GENDER_CHOICES = [
        (GENDER_MALE, "male"),
        (GENDER_FEMALE, "female"),
        (GENDER_OTHER, "other"),
    ]

    LANGUAGE_KOREAN = "KR"
    LANGUAGE_ENGLISH = "EN"
    LANGUAGE_CHOICES = [
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_ENGLISH, "English"),
    ]

    CURRENCY_KRW = "KRW"
    CURRENCY_USD = "USD"
    CURRENCY_CHOICES = [(CURRENCY_KRW, "KRW"), (CURRENCY_USD, "USD")]

    avatar = models.ImageField(upload_to="avatars", blank=True)
    nickname = models.CharField(max_length=120, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, blank=True, null=True
    )
    birthdate = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    language = models.CharField(
        max_length=2, choices=LANGUAGE_CHOICES, blank=True, null=True
    )
    currency = models.CharField(
        max_length=3, choices=CURRENCY_CHOICES, blank=True, null=True
    )
    busker = models.BooleanField(default=False, blank=True, null=True)

    def get_absoulte_url(self):
        return reverse("users:profile", {"pk": self.pk})
