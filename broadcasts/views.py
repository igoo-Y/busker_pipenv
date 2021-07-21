import broadcasts
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from . import models


def home(request):
    broadcasts = models.Broadcast.objects.all()
    return render(request, "broadcasts/home.html", {"broadcasts": broadcasts})


def main_view(request):
    context = {}
    return render(request, "broadcasts/main.html", context=context)


def broadcast_detail(request, pk):
    broadcast = get_object_or_404(models.Broadcast, pk=pk)
    return render(request, "broadcasts/detail.html", {"broadcast": broadcast})


class CreateBroadcastView(CreateView):

    model = models.Broadcast
    fields = (
        "name",
        "desc",
        "image",
        "on_air",
        "country",
        "genre",
        "picture_quality",
    )
