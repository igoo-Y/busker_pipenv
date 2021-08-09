<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView
from . import forms
=======
from django.forms import forms
from django.shortcuts import redirect, render
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from . import models, forms


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


class CreateStudioView(CreateView):

    template_name = "studios/studio_create.html"
    form_class = forms.CreateStudioForm

    def form_valid(self, form):
        studio = form.save()
        studio.host = self.request.user
        studio.save()
        return redirect(reverse("studios:detail", kwargs={"pk": studio.pk}))
>>>>>>> ingyu
