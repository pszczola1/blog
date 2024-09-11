from django.db import models
from users.models import BlogUser
from django.utils.text import slugify
from django_quill.fields import QuillField

class Post(models.Model):
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False)
    slug_title = models.SlugField(blank=True)
    hashtags = models.JSONField(default=list)
    main_image = models.ImageField(upload_to="post_images")
    content = QuillField()

    class Meta:
        ordering = ["-created_on"]

    def save(self, *args, **kwargs):
        self.slug_title = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(BlogUser, on_delete=models.CASCADE)
    content = models.TextField(max_length=511, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.content

