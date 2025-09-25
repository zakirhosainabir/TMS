from django.db import models
from django.conf import settings

class Route(models.Model):
    name = models.CharField(max_length=100)
    start_point = models.CharField(max_length=100)
    end_point = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bus(models.Model):
    number = models.CharField(max_length=20)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    capacity = models.PositiveIntegerField()
    driver_name = models.CharField(max_length=100)
    driver_photo = models.ImageField(upload_to="driver_photos/", blank=True, null=True)
    time_slot = models.TimeField()

    def __str__(self):
        return f"Bus {self.number} ({self.route})"

class Registration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    date = models.DateField()
    seat_no = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f"{self.user} -> {self.bus}"
from django.db import models

# Create your models here.
