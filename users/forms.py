from django import forms
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from django.contrib.auth import get_user_model
from .models import BlogUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()

    class Meta():
        model = BlogUser
        fields = ["username", "email", "password1", "password2"]


class SetNewPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ["password1", "password2"]