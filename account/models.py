from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class AppUser(AbstractUser):
    email = models.EmailField(
        _("email address"),
        help_text="Required. Enter a valid email address",
        unique=True,
    )
    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
