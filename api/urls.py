from django.urls import path
from . import views

urlpatterns = [
    path("api/comments/<int:post_id>/<int:page_int>", views.get_comments, name="api get_comments"),
    path("api/comments/delete/<int:comment_id>", views.delete_comment, name="api delete_comment")
]
