from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from . import forms, models


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(
            self.request,
            username=email,
            password=password,
        )
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        nickname = form.cleaned_data.get("nickname")
        password = form.cleaned_data.get("password")
        user = authenticate(
            self.request,
            email=email,
            nickname=nickname,
            username=email,
            password=password,
        )
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class UserProfileView(DetailView):

    model = models.User
    context_object_name = "user_obj"


class UpdateProfileView(UpdateView):

    model = models.User
    template_name = "users/update_profile.html"
    fields = (
        "avatar",
        "nickname",
        "bio",
        "gender",
        "birthdate",
        "phone",
        "language",
        "currency",
        "busker",
    )

    def get_object(self, queryset=None):
        return self.request.user
