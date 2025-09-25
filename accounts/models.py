from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student','Student'),
        ('faculty','Faculty'),
        ('staff','Staff'),
        ('authority','Authority'),
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES)
    university_id = models.CharField(max_length=30, unique=True, null=True, blank=True)
    photo = models.ImageField(upload_to="user_photos/", blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"
