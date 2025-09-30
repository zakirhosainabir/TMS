from django.db import models
from transport.models import Bus   # ✅ fixed import

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
