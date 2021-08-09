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
            "genres",
            "picture_quality",
        )

    def clean_genres(self):
        genres = self.cleaned_data["genres"]
        if len(genres) > 2:
            raise forms.ValidationError("장르는 최대 2개까지 선택가능합니다.")
        return genres

    def save(self, *args, **kwargs):
        broadcast = super().save(commit=False)
        return broadcast


class UpdateBroadcastForm(forms.Form):
    pass
