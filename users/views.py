from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegistrationForm, SetNewPasswordForm
from .models import BlogUser
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            authenticate(email=user.email, password=user.password)
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, "Incorrect form")
    else:
        form = RegistrationForm()
    
    return render(request, "registration/register.html", {"form": form})


def profile(request, username=""):
    if username == "":
        if request.user:
            return redirect(f"/profile/{request.user.username}")
        else:
            return redirect("/")
    user = BlogUser.objects.get(username=username)
    if request.method == "POST":
        if "bio" in request.POST:
            user.bio = request.POST["bio"]
            user.save()
            return redirect(f"/profile/{request.user.username}")
    return render(request, "profile/profile.html", {"viewed_user": user})


@login_required(login_url="/login")
def password_change(request):
    user = request.user
    if request.method == "POST":
        form = SetNewPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    form = SetNewPasswordForm(user)
    return render(request, "password_reset_confirm.html", {"form": form})

