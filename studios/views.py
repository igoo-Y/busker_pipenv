from django.forms import forms
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
    FormView,
)
from . import models, forms


class DeletePostView(DeleteView):

    model = models.Post
    template_name = "studios/post_confirm_delete.html"

    def get_success_url(self):
        pk = self.kwargs.get("studio_pk")
        return reverse("studios:posts", kwargs={"pk": pk})


class UpdatePostView(UpdateView):

    model = models.Post
    template_name = "studios/post_update.html"
    fields = (
        "title",
        "body",
        "category",
    )

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        studio_pk = self.kwargs.get("studio_pk")
        return reverse("studios:post-detail", kwargs={"pk": pk, "studio_pk": studio_pk})


class DetailPostView(DetailView):

    model = models.Post
    template_name = "studios/post_detail.html"


class AddPostView(FormView):

    form_class = forms.CreatePostForm
    template_name = "studios/post_create.html"

    def form_valid(self, form):
        pk = self.kwargs.get("pk")
        user = self.request.user
        form.save(pk, user)
        return redirect(reverse("studios:posts", kwargs={"pk": pk}))


class StudioPostsView(DetailView):

    model = models.Studio
    template_name = "studios/studio_posts.html"


class DeleteStudioView(DeleteView):

    model = models.Studio
    success_url = reverse_lazy("core:home")
    template_name = "studios/studio_confirm_delete.html"


class UpdateStudioView(UpdateView):

    model = models.Studio
    template_name = "studios/studio_update.html"
    fields = (
        "name",
        "desc",
        "image",
    )

    def get_object(self, queryset=None):
        studio = super().get_object(queryset=queryset)
        if studio.host.pk != self.request.user.pk:
            raise Http404()
        else:
            return studio


class DetailStudioView(DetailView):

    model = models.Studio
    template_name = "studios/studio_detail.html"
    context_object_name = "studio"


class CreateStudioView(FormView):

    template_name = "studios/studio_create.html"
    form_class = forms.CreateStudioForm

    def form_valid(self, form):
        studio = form.save()
        studio.host = self.request.user
        studio.save()
        return redirect(reverse("studios:posts", kwargs={"pk": studio.pk}))
