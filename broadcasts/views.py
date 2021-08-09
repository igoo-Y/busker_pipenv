from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView
from django.http import Http404
from . import models, forms
import broadcasts
import random


def home(request):
    broadcasts = models.Broadcast.objects.all()
    return render(request, "broadcasts/home.html", {"broadcasts": broadcasts})


def main_view(request):
    context = {}
    return render(request, "broadcasts/main.html", context=context)


class BroadcastDetail(DetailView):

    model = models.Broadcast
    template_name = "broadcasts/broadcast_detail.html"
    context_object_name = "broadcast"

    def get_queryset(self):
        on_air_list = models.Broadcast.objects.filter(on_air=True)
        return on_air_list

    def get_random_pk(self):
        random_broadcast = (
            models.Broadcast.objects.filter(on_air=True).order_by("?").first()
        )
        random_pk = random_broadcast.pk
        print(random_pk)
        return random_pk


class CreateBroadcastView(CreateView):

    template_name = "broadcasts/broadcast_create.html"
    form_class = forms.CreateBroadcastForm

    def form_valid(self, form):
        broadcast = form.save()
        broadcast.host = self.request.user
        broadcast.save()
        form.save_m2m()
        return redirect(reverse("broadcasts:detail", kwargs={"pk": broadcast.pk}))


class UpdateBroadcastView(UpdateView):

    model = models.Broadcast
    template_name = "broadcasts/broadcast_update.html"
    fields = (
        "name",
        "desc",
        "image",
        "on_air",
        "country",
        "genres",
        "picture_quality",
    )

    def get_object(self, queryset=None):
        broadcast = super().get_object(queryset=queryset)
        if broadcast.host.pk != self.request.user.pk:
            raise Http404()
        else:
            return broadcast
