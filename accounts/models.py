from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    university_id = models.CharField(max_length=20, unique=True, null=True, blank=True)

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return self.username
