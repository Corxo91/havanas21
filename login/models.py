from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    if_cocina = models.BooleanField(null=False, blank=False, default=False)
    if_bar = models.BooleanField(null=False, blank=False, default=False)
    if_admin = models.BooleanField(null=False, blank=False, default=True)