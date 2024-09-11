from django.shortcuts import render, redirect
from django.http.response import HttpResponseNotFound
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .models import Post, Comment
from .forms import AddCommentForm, PostCreationForm
from math import ceil

# Create your views here.


def homepage(request):
    print(request.user)
    return page(request, 1)


def page(request, page_int):
    posts = Post.objects.all()
    if page_int*8 > posts.count():  # returns last page, when user manually types in a number beyond the last page
        page_int = ceil(posts.count()/8)
    if page_int < 1:
        page_int = 1
    return render(request, "core/page.html", {"posts": posts[(page_int-1)*8:page_int*8], "page": page_int})


def post(request, slug_title):
    current_post = ""
    try:
        current_post = Post.objects.get(slug_title=slug_title)
        print(current_post.content)
    except Exception as e:
        #happens when user types in a slug title that doesn't exist
        return HttpResponseNotFound(e)
    if request.method == "GET":
        form = AddCommentForm(request.GET)
        if form.is_valid():
            author = request.user
            content = form.cleaned_data["content"]
            new_comment = Comment(post=current_post, author=author, content=content)
            new_comment.save()
            """
            https://en.wikipedia.org/wiki/Post/Redirect/Get (PRG)
            makes it so that form is not submitted again on refresh
            """
            messages.success(request, "Comment posted sucessfuly!")
            return redirect(f"/post/{slug_title}")
    return render(request, "core/post.html", {"post": current_post, "form": AddCommentForm()})


@permission_required("core.add_post", raise_exception=True) #raise_exeption=True redirects to 403 Forbidden page
def add_post(request):
    if request.method == "POST":
        form = PostCreationForm(request.POST, request.FILES)
        print("is valid:", form.is_valid())
        if form.is_valid():
            print(form)
            author = request.user
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            main_image = form.cleaned_data["main_image"]
            new_post = Post(author=author, title=title, content=content, main_image=main_image)
            print(new_post)
            new_post.save()
            messages.success(request, "Post created sucessfuly")
            return redirect("/")
    return render(request, "core/add.html", {"form": PostCreationForm()})
