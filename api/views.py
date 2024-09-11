#from django.shortcuts import render
from django.core import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Comment
from users.models import BlogUser
import json
from math import ceil

# Create your views here.


@api_view(["GET"])
def get_comments(request, post_id, page_int):
    """
    returns comments that have foreign keys(id's of Post instances)
    equal to post_id
    """
    try:
        comments = Comment.objects.filter(post__pk=post_id)
        max_page = ceil(comments.count()/20)
    except:
        return Response(status=404)

    if page_int < 1 or page_int > max_page:
        return Response(status=404)

    comments = comments[(page_int-1)*20:page_int*20]

    comments_json = serializers.serialize('json', comments)  # changes QuerySet to JSON format
    comments_json = json.loads(comments_json) # json in a string -> python dictonary

    # replaces id's of comment author's with their usernames
    for comment in comments_json:
        author_id = comment["fields"]["author"]
        comment["fields"]["author"] = BlogUser.objects.get(id=author_id).username
        
    return Response(comments_json)  # rest_framework's Response automatically converts response into json


@api_view(["GET"])
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    #print(request.user.is_superuser, comment.author.username, request.user.username)
    if request.user.is_superuser or comment.author.username == request.user.username:
        comment.delete()
        return Response(status=200)
    return Response(status=403)