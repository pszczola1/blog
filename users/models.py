from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class BlogUser(AbstractUser):

    email = models.EmailField("Email adress", max_length=254, unique=True)
    username = models.CharField("Username", max_length=31)
    date_joined = models.DateField(auto_now_add=True)
    profile_image = models.ImageField(upload_to="profile_images", default="default_profile_picture.jpeg")
    bio = models.TextField("Bio", blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    