from django import forms
from django.forms import models
from . import models


class CreateBroadcastForm(forms.ModelForm):
    class Meta:
        model = models.Broadcast
        fields = (
            "name",
            "desc",
            "image",
            "on_air",
            "country",
            "genre",
            "picture_quality",
        )

    def save(self, *args, **kwargs):
        broadcast = super().save(commit=False)
        return broadcast
