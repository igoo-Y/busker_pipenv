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
from django.core.paginator import Paginator
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


def StudioPostsView(request, pk):
    page = request.GET.get("page")
    studio = models.Studio.objects.get(pk=pk)
    studio_posts = models.Post.objects.filter(studio=studio)
    paginator = Paginator(studio_posts, 10)
    posts = paginator.get_page(page)
    return render(
        request,
        "studios/studio_posts.html",
        {
            "pk": pk,
            "studio_posts": studio_posts,
            "studio": studio,
            "posts": posts,
        },
    )


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

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        return reverse("studios:posts", kwargs={"pk": pk})


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
