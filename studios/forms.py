from django import forms
from django.forms import fields, widgets
from . import models


class CreateStudioForm(forms.ModelForm):
    class Meta:
        model = models.Studio
        fields = (
            "name",
            "desc",
            "image",
        )

    def save(self, *args, **kwargs):
        studio = super().save(commit=False)
        return studio


class UpdateStudioForm(forms.Form):
    pass
