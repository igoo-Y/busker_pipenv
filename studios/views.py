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

    template_name = "studios/studio_create.html"
    form_class = forms.CreateStudioForm

    def form_valid(self, form):
        studio = form.save()
        studio.host = self.request.user
        studio.save()
        return redirect(reverse("studios:detail", kwargs={"pk": studio.pk}))
