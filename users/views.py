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


# def kakao_login(request):
#     client_id = os.environ.get("KAKAO_KEY")
#     redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback"
#     return redirect(
#         f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
#     )


# class KakaoException(Exception):
#     pass


# def kakao_callback(request):
#     try:
#         code = request.GET.get("code")
#         client_id = os.environ.get("KAKAO_KEY")
#         redirect_uri = "http://127.0.0.1:8000/users/login/kakao/callback"
#         token_request = requests.post(
#             f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}"
#         )
#         token_json = token_request.json()
#         error = token_json.get("error", None)
#         if error is not None:
#             raise KakaoException()
#         access_token = token_json.get("access_token")
#         profile_request = requests.get(
#             "https://kapi.kakao.com/v2/user/me",
#             headers={"Authorization": f"Bearer {access_token}"},
#         )
#         profile_json = profile_request.json()
#         kakao_account = profile_json.get("kakao_account")
#         email = kakao_account.get("email")
#         if email is None:
#             raise KakaoException()
#         properties = profile_json.get("properties")
#         nickname = properties.get("nickname")
#         profile_image = properties.get("profile_image")
#         try:
#             user = models.User.objects.get(email=email)
#             if user.login_method != models.User.LOGIN_KAKAO:
#                 raise KakaoException()
#         except models.User.DoesNotExist:
#             user = models.User.objects.create(
#                 email=email,
#                 username=email,
#                 nickname=nickname,
#                 first_name=nickname,
#                 login_method=models.User.LOGIN_KAKAO,
#             )
#             user.set_unusable_password()
#             user.save()
#             if profile_image is not None:
#                 photo_request = requests.get(profile_image)
#                 user.avatar.save(
#                     f"{nickname}_avatar", ContentFile(photo_request.content)
#                 )
#         login(request, user)
#         return redirect(reverse("core:home"))
#     except KakaoException:
#         return redirect(reverse("users:login"))
