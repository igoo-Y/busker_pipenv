from django.shortcuts import render


def home(request):
    return render(request, "broadcasts/home.html")


def main_view(request):
    context = {}
    return render(request, "broadcasts/main.html", context=context)
