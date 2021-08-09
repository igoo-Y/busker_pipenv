<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Studio
from . import forms

# import studios

# def home(request):
# return render(request, "home.html", {})

# class 기반 views
# detailview는 studio 띄워주는

""""
def main_view(request):
    context = {}
    return render(request, "home.html", context=context)
"""


class DetailStudioView(DetailView):
    model = Studio
    template_name = "detail.html"


class CreateStudioView(CreateView):
    model = Studio
    template_name = "studio_create.html"
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
>>>>>>> ingyu

    template_name = "studios/studio_create.html"
    form_class = forms.CreateStudioForm

    def form_valid(self, form):
        studio = form.save()
        studio.host = self.request.user
        studio.save()
        return redirect(reverse("studios:detail", kwargs={"pk": studio.pk}))
