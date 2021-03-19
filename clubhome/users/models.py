from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(null=True, blank=True, max_length=256)
    profile_description = models.TextField(null=True, blank=True)
    twitter = models.CharField(null=True, blank=True, max_length=256)
    instagram = models.CharField(null=True, blank=True, max_length=256)
    profile_picture = models.ImageField(null=True, upload_to="profile_picture")
