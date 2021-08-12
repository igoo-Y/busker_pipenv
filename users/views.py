import os
import requests
from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.views.generic.edit import UpdateView
from django.core.files.base import ContentFile
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
        "first_name",
        "last_name",
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

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.fields["first_name"].widget.attrs = {"placeholder": "이름"}
        form.fields["last_name"].widget.attrs = {"placeholder": "성"}
        form.fields["nickname"].widget.attrs = {"placeholder": "닉네임"}
        form.fields["bio"].widget.attrs = {"placeholder": "당신에 대해 알려주세요!"}
        form.fields["birthdate"].widget.attrs = {"placeholder": "생년월일 ex)2000-01-01"}
        form.fields["phone"].widget.attrs = {"placeholder": "연락처 ex)010-0000-0000"}
        return form

    def get_object(self, queryset=None):
        return self.request.user


class UpdatePassword(PasswordChangeView):

    template_name = "users/update_password.html"

    def get_success_url(self):
        return self.request.user.get_absolute_url()
