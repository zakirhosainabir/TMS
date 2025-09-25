from django.db import models
import transport.models

from uap_tms.transport.models import Bus


class Location(models.Model):
    bus = models.OneToOneField(
        Bus,
        on_delete=models.CASCADE,
        related_name='location'
    )
    lat = models.FloatField()
    lng = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bus.number} Location: ({self.lat}, {self.lng})"
from django.db import models

# Create your models here.
