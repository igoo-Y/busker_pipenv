from django.http import request
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from . import models, forms


def home(request):
    broadcasts = models.Broadcast.objects.all()
    return render(request, "broadcasts/home.html", {"broadcasts": broadcasts})


def main_view(request):
    context = {}
    return render(request, "broadcasts/main.html", context=context)


class BroadcastDetail(DetailView):

    model = models.Broadcast


class CreateBroadcastView(CreateView):

    template_name = "broadcasts/broadcast_create.html"
    form_class = forms.CreateBroadcastForm

    def form_valid(self, form):
        broadcast = form.save()
        broadcast.host = self.request.user
        broadcast.save()
        form.save_m2m()
        return redirect(reverse("broadcasts:detail", kwargs={"pk": broadcast.pk}))
