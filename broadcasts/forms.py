from django import forms
from django.forms import models
from . import models
from django_countries.fields import CountryField


class CreateBroadcastForm(forms.ModelForm):
    class Meta:
        model = models.Broadcast
        fields = (
            "name",
            "desc",
            "image",
            "on_air",
            "genres",
            "picture_quality",
        )

    name = forms.CharField(label="채널 이름")
    desc = forms.CharField(label="채널 설명")

    def save(self, *args, **kwargs):
        broadcast = super().save(commit=False)
        return broadcast


class UpdateBroadcastForm(forms.Form):
    pass
