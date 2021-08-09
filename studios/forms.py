from django import forms
from django.forms import models
from . import models


class CreateStudioForm(forms.ModelForm):
    class Meta:
        model = models.Studio
        fields = ("name",)

    def save(self, *args, **kwargs):
        studio = super().save(commit=False)
        return studio


class UpdateBroadcastForm(forms.Form):
    pass
