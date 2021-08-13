from django import forms
from django.forms import fields, widgets
from . import models


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = (
            "title",
            "body",
        )

    def save(self, pk, user, *args, **kwargs):
        post = super().save(commit=False)
        studio = models.Studio.objects.get(pk=pk)
        post.studio = studio
        post.writer = user
        post.save()


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
