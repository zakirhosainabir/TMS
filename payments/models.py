from django.db import models
from transport.models import Registration   # ✅ fixed import

class Payment(models.Model):
    registration = models.OneToOneField(
        Registration,
        on_delete=models.CASCADE,
        related_name='payment'
    )
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, default="pending")
    transaction_id = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.registration.user.username} - {self.status}"
