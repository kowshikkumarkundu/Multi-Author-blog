from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    profile_picture = models.ImageField(
        upload_to="profile_pictures/",
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    address = models.CharField(
        max_length=255,
        blank=True
    )

    is_author = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["user__username"]

    def __str__(self):
        return self.user.username