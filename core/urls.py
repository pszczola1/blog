from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home"),
    path("page/<int:page_int>", views.page, name="specific_page"),
    path("post/<slug:slug_title>", views.post, name="post"),  #slug - no spaces, wierd symbols etc.
    path("add", views.add_post, name="add post")
]
