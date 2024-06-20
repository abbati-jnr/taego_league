from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager


class User(BaseUser):
    ADMIN = 1
    MANAGER = 2
    PLAYER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (PLAYER, 'Player'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES)
    profile_pic = models.ImageField(upload_to='profile/')
    objects = BaseUserManager()

