from django import forms
<<<<<<< HEAD
from django.forms import models
=======
from django.forms import fields
>>>>>>> ingyu
from . import models


class CreateStudioForm(forms.ModelForm):
    class Meta:
        model = models.Studio
<<<<<<< HEAD
        fields = ("name",)
=======
        fields = (
            "name",
            "desc",
            "image",
        )
>>>>>>> ingyu

    def save(self, *args, **kwargs):
        studio = super().save(commit=False)
        return studio


<<<<<<< HEAD
class UpdateBroadcastForm(forms.Form):
=======
class UpdateStudioForm(forms.Form):
>>>>>>> ingyu
    pass
