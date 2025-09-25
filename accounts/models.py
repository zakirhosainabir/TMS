from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # You can add extra fields if needed, for now keep it simple
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
