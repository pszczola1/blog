from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _  #translates the text

class CustomUserManager(BaseUserManager):
    """
    custom user model manager
    email is a unique identifier
    """
    def create_user(self, email, password, **extra_fields):
        """
        create and save user
        """
        if not email:
            raise ValueError(_("Email is required"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        create and save superuser
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff") or not extra_fields.get("is_superuser"):
            raise ValueError(_("Both is_staff and is_superuser must be set to True"))
        return self.create_user(email, password, **extra_fields)