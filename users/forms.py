from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.forms import models
from django.forms.widgets import PasswordInput
from . import models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("패스워드를 확인해주세요."))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("해당 유저가 존재하지 않습니다."))


class SignUpForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            "email",
            "nickname",
            "first_name",
            "last_name",
        ]

    password = forms.CharField(widget=PasswordInput)
    password1 = forms.CharField(widget=PasswordInput, label="Confirm Password")
    busker = forms.BooleanField(label="버스커(가수)입니까?")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("User already exists with that email.")
        except models.User.DoesNotExist:
            return email

    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")
        try:
            models.User.objects.get(nickname=nickname)
            raise forms.ValidationError("User already exists with that nickname.")
        except models.User.DoesNotExist:
            return nickname

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        user = super().save(commit=False)
        email = self.cleaned_data.get("email")
        nickname = self.cleaned_data.get("nickname")
        password = self.cleaned_data.get("password")
        user.username = email
        user.nickname = nickname
        user.set_password(password)
        user.save()
