from django.urls import path
from . import views

urlpatterns = [
    path("profile/<str:username>", views.profile, name="profile"),
    path("password_change", views.password_change, name="password_change")
]
